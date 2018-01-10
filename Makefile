
libfoo.so: *.go    
	GOOS=linux GOARCH=amd64 CGO_ENABLED=1 go build -buildmode=c-shared -o libfoo.so .
