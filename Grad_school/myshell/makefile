CC = gcc
CFLAGS = -Wall

all: myshell

myshell: main.c shell_commands.c util.c
	$(CC) $(CFLAGS) -o myshell main.c shell_commands.c util.c

clean:
	rm -f myshell
