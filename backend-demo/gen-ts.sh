protoc -I=proto --js_out=import_style=typescript:ts-client --grpc-web_out=import_style=typescript,mode=grpcwebtext:ts-client hello.proto
