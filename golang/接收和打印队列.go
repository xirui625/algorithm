package main

import (
	"fmt"
	"time"
)

func main() {
	receiveQueue := make(chan int)
	printQueue := make(chan int)

	// Goroutine 1: 接收数据并发送到 printQueue
	go func() {
		for i := 1; i <= 100; i++ {
			receiveQueue <- i
			time.Sleep(10 * time.Millisecond) // 模拟接收数据的延迟
		}
		close(receiveQueue)
	}()

	// Goroutine 2: 从 receiveQueue 接收数据并发送到 printQueue
	go func() {
		for num := range receiveQueue {
			printQueue <- num
		}
		close(printQueue)
	}()

	// 从 printQueue 接收数据并打印
	for num := range printQueue {
		fmt.Println(num)
	}
}
