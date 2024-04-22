package main

import (
	"fmt"
	"sync"
	"time"
)

var mutex sync.Mutex

func worker(id int, jobs []int, results *[]int) {
	for _, job := range jobs {
		fmt.Printf("Worker %d started job %d\n", id, job)
		time.Sleep(time.Second) // 模拟耗时任务
		fmt.Printf("Worker %d finished job %d\n", id, job)
		mutex.Lock()
		*results = append(*results, job*2) // 将结果追加到结果切片
		mutex.Unlock()
	}
}

func main() {
	numJobs := 5
	jobs := make([]int, numJobs)
	for i := 0; i < numJobs; i++ {
		jobs[i] = i + 1
	}

	results := make([]int, 0, numJobs)

	var wg sync.WaitGroup
	for w := 1; w <= 3; w++ {
		wg.Add(1)
		go func(w int) {
			defer wg.Done()
			worker(w, jobs, &results)
		}(w)
	}
	wg.Wait()

	fmt.Println("All jobs done. Results:", results)
}
