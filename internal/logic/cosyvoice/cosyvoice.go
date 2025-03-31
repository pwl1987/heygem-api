package cosyvoice

import (
	"bytes"
	"context"
	"fmt"
	"github.com/gogf/gf/v2/errors/gerror"
	"github.com/gogf/gf/v2/frame/g"
	"github.com/gogf/gf/v2/os/gtime"
	"github.com/gogf/gf/v2/util/grand"
	"heygem-api/internal/boot"
	"heygem-api/internal/consts"
	"heygem-api/internal/dao"
	"heygem-api/internal/model/entity"
	"heygem-api/internal/model/input/cosyin"
	"heygem-api/internal/model/input/ttsin"
	"heygem-api/internal/pkg/tts"
	util "heygem-api/utility"
	"net/url"
	"strconv"
	"strings"
	"time"
)

type sCosyvoice struct {
}

func init() {

}

func (s *sCosyvoice) SpeechRecognition(ctx context.Context, inp *cosyin.SpeechRecognitionInp) (res *cosyin.SpeechRecognitionOut, err error) {

	return
}

func (s *sCosyvoice) Inference(ctx context.Context, inp *cosyin.InferenceInp) (res *cosyin.InferenceOut, err error) {

	return
}
