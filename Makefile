
libfoo.so: *.go    
	GOOS=linux GOARCH=amd64 go build -buildmode=c-shared -o libfoo.so .
