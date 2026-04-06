/*****************************************************************************
 *
 *     This file is part of the University of Michigan (U-M) EECS 489.
 *
 *     U-M EECS 489 is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, either version 3 of the License, or
 *     (at your option) any later version.
 *
 *     U-M EECS 489 is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY; without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with U-M EECS 489. If not, see <https://www.gnu.org/licenses/>.
 *
 *****************************************************************************/

/*
 * client.c
 * Name: Kovidh Maydiga
 * PUID: 71992397
 */

#include <errno.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

#define SEND_BUFFER_SIZE 2048

/* TODO: client()
 * Open socket and send message from stdin.
 * Return 0 on success, non-zero on failure
 */
int client(char *server_ip, char *server_port) {
  struct addrinfo hints, *server_info, *p;
  int sockfd;
  char buffer[SEND_BUFFER_SIZE];
  ssize_t bytes_read, bytes_sent, total_sent;

  memset(&hints, 0, sizeof(hints));
  hints.ai_family = AF_UNSPEC;     
  hints.ai_socktype = SOCK_STREAM; 

  int status = getaddrinfo(server_ip, server_port, &hints, &server_info);
  if (status != 0) {
    fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(status));
    return 1;
  }

  for (p = server_info; p != NULL; p = p->ai_next) {
    sockfd = socket(p->ai_family, p->ai_socktype, p->ai_protocol);
    if (sockfd == -1) {
      perror("client: socket");
      continue;
    }

    if (connect(sockfd, p->ai_addr, p->ai_addrlen) == -1) {
      close(sockfd);
      perror("client: connect");
      continue;
    }

    break;
  }

  freeaddrinfo(server_info);

  if (p == NULL) {
    fprintf(stderr, "client: failed to connect\n");
    return 1;
  }

  while ((bytes_read = read(STDIN_FILENO, buffer, SEND_BUFFER_SIZE)) > 0) {
    total_sent = 0;

    while (total_sent < bytes_read) {
      bytes_sent = send(sockfd, buffer + total_sent, bytes_read - total_sent, 0);
      if (bytes_sent == -1) {
        perror("send");
        close(sockfd);
        return 1;
      }
      total_sent += bytes_sent;
    }
  }

  if (bytes_read == -1) {
    perror("read");
    close(sockfd);
    return 1;
  }

  close(sockfd);
  return 0;
}

/*
 * main()
 * Parse command-line arguments and call client function
 */
int main(int argc, char **argv) {
  char *server_ip;
  char *server_port;

  if (argc != 3) {
    fprintf(stderr,
            "Usage: ./client-c (server IP) (server port) < (message)\n");
    exit(EXIT_FAILURE);
  }

  server_ip = argv[1];
  server_port = argv[2];
  return client(server_ip, server_port);
}
