package main

import (
	"crypto/rand"
	"fmt"
	"os"
	"path/filepath"
	"sync"
	"time"
)

// generateEncryptedFile simulates the creation of an encrypted file by generating
// 1MB of pseudorandom data and writing it to the specified file path.
// This function is run concurrently for each file.
func generateEncryptedFile(filePath string, wg *sync.WaitGroup) {
	defer wg.Done()

	// Create a 1MB file of pure pseudorandom data to simulate encryption
	data := make([]byte, 1024*1024)
	_, err := rand.Read(data)
	if err != nil {
		fmt.Println("Error generating random data:", err)
		return
	}

	err = os.WriteFile(filePath, data, 0644)
	if err != nil {
		fmt.Println("Error writing file:", err)
	}
}

func main() {
	// Define the target directory for victim files relative to the script location
	targetDir := filepath.Join("..", "victim_files")
	os.MkdirAll(targetDir, os.ModePerm)

	fmt.Println("Initiating concurrent encryption simulation...")
	var wg sync.WaitGroup

	startTime := time.Now()

	// Spawn 100 goroutines to simulate a ransomware attack
	for i := 1; i <= 100; i++ {
		wg.Add(1)
		fileName := fmt.Sprintf("encrypted_data_%d.locked", i)
		filePath := filepath.Join(targetDir, fileName)
		go generateEncryptedFile(filePath, &wg)
	}

	wg.Wait()
	elapsedTime := time.Since(startTime)
	fmt.Printf("Simulation complete. 100 files encrypted in %s\n", elapsedTime)
}
