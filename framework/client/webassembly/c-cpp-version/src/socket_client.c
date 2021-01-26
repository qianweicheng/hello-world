#include <stdio.h>     // perror, printf
#include <stdlib.h>    // exit, atoi
#include <unistd.h>    // write, read, close
#include <arpa/inet.h> // sockaddr_in, AF_INET, SOCK_STREAM, INADDR_ANY, socket etc...
#include <string.h>    // strlen, memset
#include <emscripten.h>

const char message[] = "Hello sockets world\n";

EMSCRIPTEN_KEEPALIVE
void send_data() {

    int serverFd;
    struct sockaddr_in server;
    int len;
    int port = 1234;
    char *server_ip = "127.0.0.1";
    char *buffer = "hello from client\n";
    
    serverFd = socket(AF_INET, SOCK_STREAM, 0);
    if (serverFd < 0)
    {
        perror("Cannot create socket");
    }
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr(server_ip);
    server.sin_port = htons(port);
    len = sizeof(server);
    if (connect(serverFd, (struct sockaddr *)&server, len) < 0)
    {
        perror("Cannot connect to server");
    }
    while(1) {
        printf("Client Ping:%s\r\n", buffer);
        if (write(serverFd, buffer, strlen(buffer)) < 0)
        {
            perror("Cannot write");
        }
        char recv[1024];
        memset(recv, 0, sizeof(recv));
        if (read(serverFd, recv, sizeof(recv)) < 0)
        {
            perror("cannot read");
        }
        printf("Server Echo:%s\r\n", recv);
        if (recv[0] == 'q') {
            printf("exit client\r\n");
            break;
        }
    }
    close(serverFd);    
}

int main(int argc, char *argv[]) {
    send_data();
}