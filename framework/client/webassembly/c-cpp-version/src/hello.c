#include <stdio.h>
#include <emscripten.h>

extern void my_js(void);

EMSCRIPTEN_KEEPALIVE
char* hello(const char * name) {
    my_js();
    printf("Hello %s\n", name);
    return "This is the value returned by hello";
}

EMSCRIPTEN_KEEPALIVE
int add(int x, int y) {
    printf("C add(%d,%d)\r\n", x, y);
    return x + y;
}

EMSCRIPTEN_KEEPALIVE
int square(int x) {
    return x * x;
}

EMSCRIPTEN_KEEPALIVE
int fib(int n)
{
    if (n <= 0)
    {
        return 0;
    }
    int i, t, a = 0, b = 1;
    for (i = 1; i < n; i++)
    {
        t = a + b;
        a = b;
        b = t;
    }
    return b;
}

EMSCRIPTEN_KEEPALIVE
void call_js() {
    emscripten_run_script("console.log('hi, call js from c')");
}

int main(int argc, char *argv[]) {
    printf("Hello from C main()\r\n");
    return 0;
}