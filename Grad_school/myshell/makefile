CC = gcc
CFLAGS = -Wall

all: mydispatcher

mydispatcher: mydispatcher.c utils.c algorithms.c
	$(CC) $(CFLAGS) -o mydispatcher mydispatcher.c utils.c algorithms.c

clean:
	rm -f mydispatcher
