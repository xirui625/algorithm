package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	var mu sync.Mutex
	condition := sync.NewCond(&mu)

	counter := 1
	max := 100

	wg.Add(2)

	// Goroutine 1
	go func() {
		defer wg.Done()
		for {
			mu.Lock()
			for counter%2 == 0 && counter <= max {
				condition.Wait()
			}
			if counter > max {
				condition.Signal() // Wake up other goroutine before exit
				mu.Unlock()
				return
			}
			fmt.Println("Goroutine 1:", counter)
			counter++
			condition.Signal()
			mu.Unlock()
		}
	}()

	// Goroutine 2
	go func() {
		defer wg.Done()
		for {
			mu.Lock()
			for counter%2 == 1 && counter <= max {
				condition.Wait()
			}
			if counter > max {
				condition.Signal() // Wake up other goroutine before exit
				mu.Unlock()
				return
			}
			fmt.Println("Goroutine 2:", counter)
			counter++
			condition.Signal()
			mu.Unlock()
		}
	}()

	wg.Wait()
}

