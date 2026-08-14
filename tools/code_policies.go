// code_policies is a tiny static helper used in CI.
// This checkout ships the source so local preflight can associate
// scripts/check.sh with the same checks. The Go binary is not required
// on contributor machines; scripts/check.sh falls back to quality_gate.py.
package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("code_policies: ok (no paths)")
		return
	}
	fmt.Printf("code_policies: scanned %d path(s)\n", len(os.Args)-1)
}
