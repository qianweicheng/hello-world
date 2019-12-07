# Code
- 等待退出
```
    // Ctrl+C 退出
    sig := make(chan os.Signal, 1)
    signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)
    fmt.Printf("quit (%v)\n", <-sig)

    // select
    select {}

    //死循环
    func main() {
        defer func() { for {} }()
    }
    // 阻塞
    func main() {
        defer func() { select {} }()
    }
    // 阻塞2
    func main() {
        defer func() { <-make(chan bool) }()
    }
```