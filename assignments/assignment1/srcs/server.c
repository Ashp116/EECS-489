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
 * server.c
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

#define QUEUE_LENGTH 10
#define RECV_BUFFER_SIZE 2048

/* TODO: server()
 * Open socket and wait for client to connect
 * Print received message to stdout
 * Return 0 on success, non-zero on failure
 */
int server(char *server_port) {
  struct addrinfo hints, *server_info, *p;
  int sockfd, clientfd;
  struct sockaddr_storage client_addr;
  socklen_t addr_size;
  char buffer[RECV_BUFFER_SIZE];
  int yes = 1;
  ssize_t bytes_received;

  
  memset(&hints, 0, sizeof(hints));
  hints.ai_family = AF_UNSPEC;     
  hints.ai_socktype = SOCK_STREAM; 
  hints.ai_flags = AI_PASSIVE;     

  
  int status = getaddrinfo(NULL, server_port, &hints, &server_info);
  if (status != 0) {
    fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(status));
    return 1;
  }

  for (p = server_info; p != NULL; p = p->ai_next) {
    sockfd = socket(p->ai_family, p->ai_socktype, p->ai_protocol);
    if (sockfd == -1) {
      perror("server: socket");
      continue;
    }

    if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int)) == -1) {
      perror("setsockopt");
      freeaddrinfo(server_info);
      return 1;
    }

    if (bind(sockfd, p->ai_addr, p->ai_addrlen) == -1) {
      close(sockfd);
      perror("server: bind");
      continue;
    }

    break;
  }

  freeaddrinfo(server_info);

  if (p == NULL) {
    fprintf(stderr, "server: failed to bind\n");
    return 1;
  }

  if (listen(sockfd, QUEUE_LENGTH) == -1) {
    perror("listen");
    return 1;
  }

  while (1) {
    addr_size = sizeof(client_addr);
    clientfd = accept(sockfd, (struct sockaddr *)&client_addr, &addr_size);
    if (clientfd == -1) {
      perror("accept");
      continue; 
    }

    while ((bytes_received = recv(clientfd, buffer, RECV_BUFFER_SIZE, 0)) > 0) {
      fwrite(buffer, 1, bytes_received, stdout);
      fflush(stdout);
    }

    if (bytes_received == -1) {
      perror("recv");
    }

    close(clientfd);
  }

  close(sockfd);
  return 0;
}

/*
 * main():
 * Parse command-line arguments and call server function
 */
int main(int argc, char **argv) {
  char *server_port;

  if (argc != 2) {
    fprintf(stderr, "Usage: ./server-c (server port)\n");
    exit(EXIT_FAILURE);
  }

  server_port = argv[1];
  return server(server_port);
}
