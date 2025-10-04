package rpc

import (
	"context"
	"log"

	"rocketmq-gateway/mq"
	mqproto "rocketmq-gateway/proto"
)

func strPtr(s string) *string {
	return &s
}

type RocketMQGatewayServerImpl struct {
	mqproto.UnimplementedRocketMQGatewayServer
}

// SendMessage RPC 实现
func (s *RocketMQGatewayServerImpl) SendMessage(ctx context.Context, req *mqproto.SendRequest) (*mqproto.SendResponse, error) {
	msgID, err := mq.SendMessage(req.Topic, req.GetTags(), string(req.Body))
	if err != nil {
		return &mqproto.SendResponse{
			Success: false,
			Error:   strPtr(err.Error()),
		}, nil
	}
	return &mqproto.SendResponse{
		MsgId:   msgID,
		Success: true,
	}, nil
}

// Subscribe  TODO: 实现（流式），先留空
func (s *RocketMQGatewayServerImpl) Subscribe(req *mqproto.SubscribeRequest, stream mqproto.RocketMQGateway_SubscribeServer) error {
	log.Printf("订阅: topic=%s, group=%s, tags=%s", req.Topic, req.ConsumerGroup, req.Tags)
	// 这里需要启动 consumer，从 MQ 拉取消息后写入 stream.Send()
	return nil
}
