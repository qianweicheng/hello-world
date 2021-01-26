// TCP client that sends a few messages to a server and prints out the replies
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netdb.h>

#ifdef __EMSCRIPTEN__
#include <emscripten.h>
#include <emscripten/websocket.h>
#include <emscripten/threading.h>
 
EMSCRIPTEN_WEBSOCKET_T bridgeSocket = 0;


#ifdef __cplusplus
extern "C" {
#endif

EMSCRIPTEN_WEBSOCKET_T emscripten_init_websocket_to_posix_socket_bridge(const char *bridgeUrl);

#endif

int lookup_host(const char *host)
{
  struct addrinfo hints, *res;
  int errcode;
  char addrstr[100];
  void *ptr;

  memset(&hints, 0, sizeof (hints));
  hints.ai_family = PF_UNSPEC;
  hints.ai_socktype = SOCK_STREAM;
  hints.ai_flags |= AI_CANONNAME;

  errcode = getaddrinfo(host, NULL, &hints, &res);
  if (errcode != 0)
  {
    printf("getaddrinfo failed!\n");
    return -1;
  }

  printf("Host: %s\n", host);
  while (res)
  {
    inet_ntop(res->ai_family, res->ai_addr->sa_data, addrstr, 100);

    switch (res->ai_family)
    {
    case AF_INET:
      ptr = &((struct sockaddr_in *)res->ai_addr)->sin_addr;
      break;
    case AF_INET6:
      ptr = &((struct sockaddr_in6 *)res->ai_addr)->sin6_addr;
      break;
    }
    inet_ntop(res->ai_family, ptr, addrstr, 100);
    printf("IPv%d address: %s (%s)\n", res->ai_family == PF_INET6 ? 6 : 4, addrstr, res->ai_canonname);
    res = res->ai_next;
  }

  return 0;
}

EMSCRIPTEN_KEEPALIVE void sendData() {
#ifdef __EMSCRIPTEN__
  printf("11111\r\n");
  bridgeSocket = emscripten_init_websocket_to_posix_socket_bridge("ws://localhost:8088");
  printf("22222\r\n");
  // Synchronously wait until connection has been established.
  uint16_t readyState = 0;
  int k = 100;
  do {
    printf("loop1: %d\r\n", k);
    emscripten_websocket_get_ready_state(bridgeSocket, &readyState);
    printf("loop2: %d\r\n", k);
    emscripten_thread_sleep(100);
    printf("loop3: %d\r\n", k);
    k--;
  } while(readyState == 0 && k > 0);
#endif
  printf("33333\r\n");
  if(k==0) {
    printf("end with failure.\r\n");
  }
  lookup_host("google.com");

  // Create socket
  int sock = socket(AF_INET, SOCK_STREAM, 0);
  if (sock == -1)
  {
    printf("Could not create socket");
    // exit(1);
  }
  printf("Socket created: %d\n", sock);

  struct sockaddr_in server;
  server.sin_addr.s_addr = inet_addr("127.0.0.1");
  server.sin_family = AF_INET;
  server.sin_port = htons(4444);

  if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0)
  {
    perror("connect failed. Error");
    // exit(1);
  }

  puts("Connected\n");
  for(int i = 0; i < 10; ++i)
  {
    const char message[] = "hell";
    if (send(sock, message, strlen(message), 0) < 0)
    {
      puts("Send failed");
      // exit(1);
    }

    char server_reply[256];
    if (recv(sock, server_reply, 256, 0) < 0)
    {
      puts("recv failed");
      break;
    }
     
    puts("Server reply: ");
    puts(server_reply);
  }

  close(sock);
#ifdef REPORT_RESULT
  REPORT_RESULT(101);
#endif
}

#ifdef __cplusplus
}
#endif

int main(int argc , char *argv[]) {
    printf("Hello from C++ main()\r\n");
    return 0;
}