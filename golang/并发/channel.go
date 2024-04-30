package main

import (
	"fmt"
	"time"
)

func worker(id int, jobs <-chan int, results chan<- int) {
	for job := range jobs {
		fmt.Printf("Worker %d started job %d\n", id, job)
		time.Sleep(time.Second) // 模拟耗时任务
		fmt.Printf("Worker %d finished job %d\n", id, job)
		results <- job * 2 // 将结果发送到结果通道
	}
}

func main() {
	numJobs := 5
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	// 启动多个 worker goroutine
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// 发送任务到任务通道
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs)

	// 收集结果
	for a := 1; a <= numJobs; a++ {
		<-results
	}
}
