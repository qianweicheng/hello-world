# Code
## 等待退出
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
## JSON
- 解析
```Option1
var param model.User
decoder := json.NewDecoder(c.Request.Body)
err := decoder.Decode(&param)
```
```Option2
var param model.User
bytes, err2 := c.GetRawData()
json.Unmarshal(bytes, &param)
```
- gin
err := c.ShouldBindJSON(param) 优势是可以增加验证
## Fork
```
// RunCmd ...
func RunCmd(ctx context.Context, cmd *exec.Cmd) error {
    if err := cmd.Start(); err != nil {
        return err
    }

    errCh := make(chan error, 1)
    go func() {
        errCh <- cmd.Wait()
    }()

    done := ctx.Done()
    for {
        select {
        case <-done:
            done = nil
            pid := cmd.Process.Pid
            if err := syscall.Kill(-1*pid, syscall.SIGKILL); err != nil {
                return err
            }
        case err := <-errCh:
            if done == nil {
                return ctx.Err()
            }
            return err
        }
    }
}
```