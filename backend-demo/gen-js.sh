protoc -I=proto --js_out=import_style=commonjs:js-client --grpc-web_out=import_style=commonjs,mode=grpcwebtext:js-client hello.proto
