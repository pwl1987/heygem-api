package cosyvoice

import (
	"context"
	protos "heygem-api/api/cosyvoice"
	"io"

	"github.com/gogf/gf/contrib/rpc/grpcx/v2"
	"github.com/gogf/gf/v2/frame/g"
	"github.com/gogf/gf/v2/os/gctx"
)

var client protos.CosyVoiceClient

func init() {
	address := g.Config().MustGet(gctx.New(), "heygem.cosyvoice").String()
	conn := grpcx.Client.MustNewGrpcClientConn(address)
	client = protos.NewCosyVoiceClient(conn)
}

func SpeechRecognition(ctx context.Context, req *protos.ASRRequest) (res *protos.ASRResponse, err error) {
	res, err = client.SpeechRecognition(ctx, req)
	return
}

// Inference 处理语音合成的流式调用，返回合成后的音频数据
// 由于是服务器流式响应，客户端需要读取流中的所有响应
func Inference(ctx context.Context, req *protos.Request) (res *protos.Response, err error) {
	// 调用gRPC流式接口
	stream, err := client.Inference(ctx, req)
	if err != nil {
		return nil, err
	}

	// 创建一个新的响应对象
	res = &protos.Response{}

	// 读取流中的第一个响应
	// 注意：这里简化为只读取第一个响应，实际应用中可能需要根据业务逻辑处理多个响应
	if res, err = stream.Recv(); err != nil {
		// 如果是流结束，返回nil和io.EOF
		if err == io.EOF {
			return nil, io.EOF
		}
		// 其他错误直接返回
		return nil, err
	}

	return res, nil
}

// InferenceStream 提供完整的流式处理功能
// 返回原始流对象，调用方可以自行处理流式数据
func InferenceStream(ctx context.Context, req *protos.Request) (protos.CosyVoice_InferenceClient, error) {
	return client.Inference(ctx, req)
}

// ProcessInferenceStream 处理完整的推理流，并通过回调函数处理每个响应
// callback 函数用于处理每个流响应
func ProcessInferenceStream(ctx context.Context, req *protos.Request, callback func(*protos.Response) error) error {
	stream, err := client.Inference(ctx, req)
	if err != nil {
		return err
	}

	// 持续读取流中的响应
	for {
		var resp *protos.Response
		resp, err = stream.Recv()
		if err == io.EOF {
			// 流结束
			break
		}
		if err != nil {
			// 发生错误
			return err
		}

		// 对每个响应调用回调函数
		if err := callback(resp); err != nil {
			return err
		}
	}

	return nil
}
