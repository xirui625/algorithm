package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

func worker(ctx context.Context, id int, jobs []int, results *[]int) {
	for _, job := range jobs {
		select {
		case <-ctx.Done():
			return // 如果收到取消信号，则退出
		default:
			fmt.Printf("Worker %d started job %d\n", id, job)
			time.Sleep(time.Second) // 模拟耗时任务
			fmt.Printf("Worker %d finished job %d\n", id, job)
			*results = append(*results, job*2) // 将结果追加到结果切片
		}
	}
}

func main() {
	numJobs := 5
	jobs := make([]int, numJobs)
	for i := 0; i < numJobs; i++ {
		jobs[i] = i + 1
	}

	results := make([]int, 0, numJobs)

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	var wg sync.WaitGroup
	for w := 1; w <= 3; w++ {
		wg.Add(1)
		go func(w int) {
			defer wg.Done()
			worker(ctx, w, jobs, &results)
		}(w)
	}

	// 模拟超时，取消任务
	time.Sleep(2 * time.Second)
	cancel()

	wg.Wait()

	fmt.Println("All jobs done. Results:", results)
}
