package cosyin

import "github.com/gogf/gf/v2/net/ghttp"

type SpeechRecognitionInp struct {
	Audio *ghttp.UploadFile `json:"audio" type:"audio" dc:"请上传音频"`
}

type SpeechRecognitionOut struct {
	Text string `json:"text"`
}

type InferenceInp struct {
	Mode        string            `json:"mode"`
	Audio       *ghttp.UploadFile `json:"audio" type:"file"         dc:"音频"`
	PromptAudio *ghttp.UploadFile `json:"promptAudio" type:"file"   dc:"音频"`
	SpkId       string            `json:"spkId"`
	Text        string            `json:"text"`
	PromptText  string            `json:"promptText"`
}

type InferenceOut struct{}
