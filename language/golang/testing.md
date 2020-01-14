# Test
单元测试的测试用例以 Test 开头，性能测试以 Benchmark开头
## Command
- 单元测试: go test combination_test.go combination.go
- 单元测试覆盖率: go test --cover combination_test.go combination.go
- 禁止缓存: go test -v -count=1 filename_test.go
- 性能测试: go test -bench=. combination_test.go combination.go
- 性能测试: go test -bench=".*" -cpuprofile=cpu.prof -c
  
## 内存分析
pprof