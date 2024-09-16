# Required Libraries
library(Matrix)

# Function to generate 10% missing values
generate_missing <- function(sequence) {
  # Calculate the number of missing values to be generated
  num_missing <- round(length(sequence) * 0.10)
  
  # Randomly select positions in the sequence
  missing_positions <- sample(1:length(sequence), num_missing)
  
  # Replace the selected positions with NA
  sequence[missing_positions] <- NA
  
  return(sequence)
}

# Dynamic Local Least Squares Imputation Function
DLLSimpute <- function(G) {
  # While there are still missing values in G
  while(sum(is.na(G)) > 0) {
    # Step 1: Sort each row by the number of missing values
    G <- G[order(rowSums(is.na(G))),]
    
    # Step 2: Find the first missing position in the first row
    missing_pos <- which(is.na(G[1,]))[1]
    
    # Step 3: Starting from the missing value position (i,j), the column j is scanned.
    # Increasing i, if the position (i,j) is a missing value, remove the whole row.
    G <- G[!is.na(G[,missing_pos]),]
    
    # Step 4: Separate the rest of the matrix into left and right matrices, selecting the largest matrix between these two.
    left_matrix <- G[,1:(missing_pos-1)]
    right_matrix <- G[,(missing_pos+1):ncol(G)]
    if(ncol(left_matrix) > ncol(right_matrix)) {
      G <- left_matrix
    } else {
      G <- right_matrix
    }
  }
  
  # Return the imputed matrix
  return(G)
}

# Singular Value Decomposition (SVD) Function
svd_impute <- function(G) {
  svd_decomp <- svd(G, nu = 0)
  d <- svd_decomp$d
  v <- svd_decomp$v
  u <- svd_decomp$u
  
  # Compute the pseudoinverse of G
  G_pinv <- v %*% diag(1/d) %*% t(u)
  
  # Return the imputed matrix
  return(G_pinv)
}

# Usage
# Assuming 'sequence' is your sequence with the class
sequence <- c('ATGCCCCAACTAAATACCGCCGTATGACCCACCATAATTACCCCCATACTCCTGACACTATTTCTCGTCACCCAACTAAAAATATTAAATTCAAATTACCATCTACCCCCCTCACCAAAACCCATAAAAATAAAAAACTACAATAAACCCTGAGAACCAAAATGAACGAAAATCTATTCGCTTCATTCGCTGCCCCCACAATCCTAG', 'ATGAACGAAAATCTATTCGCTTCATTCGCTGCCCCCACAATCCTAGGCTTACCCGCCGCAGTACTAATCATTCTATTCCCCCCTCTACTGGTCCCCACTTCTAAACATCTCATCAACAACCGACTAATTACCACCCAACAATGACTAATTCAACTGACCTCAAAACAAATAATAACTATACACAGCACTAAAGGACGAACCTGATCTCTCATACTAGTATCCTTAATCATTTTTATTACCACAACCAATCTTCTTGGGCTTCTACCCCACTCATTCACACCAACCACCCAACTATCTATAAACCTAGCCATGGCTATCCCCCTATGAGCAGGCGCAGTAGTCATAGGCTTTCGCTTTAAGACTAAAAATGCCCTAGCCCACTTCTTACCGCAAGGCACACCTACACCCCTTATCCCCATACTAGTTATCATCGAAACTATTAGCCTACTCATTCAACCAATAGCCTTAGCCGTACGTCTAACCGCTAACATTACTGCAGGCCACCTACTCATGCACCTAATTGGAAGCGCCACACTAGCATTATCAACTATCAATCTACCCTATGCACTCATTATCTTCACAATTCTAATCCTACTGACTATTCTAGAGATCGCCGTCGCCTTAATCCAAGCCTACGTTTTTACACTTCTAGTGAGCCTCTACCTGCACGACAACACATAA')
sequence <- generate_missing(sequence)
G_imputed <- DLLSimpute(sequence)
G_imputed_svd <- svd_impute(G_imputed)
