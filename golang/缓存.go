package main

import (
	"fmt"
	"sync"
	"time"
)

type Cache struct {
	data sync.Map
}

func (c *Cache) Set(key interface{}, value interface{}) {
	c.data.Store(key, value)
}

func (c *Cache) Get(key interface{}) (interface{}, bool) {
	return c.data.Load(key)
}

func main() {
	cache := Cache{}

	// 并发写入缓存
	for i := 0; i < 10; i++ {
		go func(idx int) {
			cache.Set(fmt.Sprintf("key%d", idx), idx)
		}(i)
	}

	// 并发读取缓存
	for i := 0; i < 10; i++ {
		go func(idx int) {
			if value, ok := cache.Get(fmt.Sprintf("key%d", idx)); ok {
				fmt.Printf("Key: key%d, Value: %v\n", idx, value)
			}
		}(i)
	}

	time.Sleep(time.Second) // 等待所有goroutine执行完毕
}
