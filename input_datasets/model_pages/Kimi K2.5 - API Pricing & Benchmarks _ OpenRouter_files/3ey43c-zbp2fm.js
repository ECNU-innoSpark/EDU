!function(){try{var e="undefined"!=typeof window?window:"undefined"!=typeof global?global:"undefined"!=typeof globalThis?globalThis:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&(e._posthogChunkIds=e._posthogChunkIds||{},e._posthogChunkIds[n]="019f9c7a-1007-74f3-9ad3-679a845667ea")}catch(e){}}();(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,495916,e=>{"use strict";var t=e.i(554331),n=e.i(361101),a=e.i(360951),s=e.i(377471),o=e.i(963),r=e.i(182657),i=e.i(421773),l=e.i(553215),d=e.i(928803),c=e.i(452473),p=e.i(967453);function m(e){let a,s,o,r,i=(0,n.c)(8);return i[0]!==e?({className:a,...s}=e,i[0]=e,i[1]=a,i[2]=s):(a=i[1],s=i[2]),i[3]!==a?(o=(0,c.cn)("rounded-md bg-card-hover px-1.5 py-0.5 font-mono text-xs text-foreground",a),i[3]=a,i[4]=o):o=i[4],i[5]!==s||i[6]!==o?(r=(0,t.jsx)("code",{className:o,...s}),i[5]=s,i[6]=o,i[7]=r):r=i[7],r}var u=e.i(260153),g=e.i(252358),h=e.i(477020),f=e.i(483498),x=e.i(339687),y=e.i(764838),b=e.i(910414),_=e.i(783710),j=e.i(861188);let $={"@openrouter/sdk":{label:"TypeScript SDK",order:10},"openrouter-ts":{label:"TypeScript SDK",order:10},"openrouter-python":{label:"Python SDK",order:20},"openrouter-go":{label:"Go SDK",order:30},python:{label:"Python",order:40},typescript:{label:"TypeScript (fetch)",order:50},curl:{label:"cURL",order:60},"openai-python":{label:"Python (OpenAI)",order:70},"openai-ts":{label:"TypeScript (OpenAI)",order:80},"openai-typescript":{label:"TypeScript (OpenAI)",order:80},"anthropic-ts":{label:"TypeScript (Anthropic)",order:90},"anthropic-go":{label:"Go (Anthropic)",order:100}};function P(e){return $[e.title]?.order??1e3}var v=e.i(86575);function I(e){let a,s,o,r,i,d,p,m,u=(0,n.c)(27),{examples:h,className:f,slug:x}=e,b=(0,g.usePosthogClient)(),[I,E]=(0,y.useState)(null);u[0]!==h?(a=[...h].sort((e,t)=>P(e)-P(t)),u[0]=h,u[1]=a):a=u[1];let A=a;u[2]!==I||u[3]!==A?(s=A.find(e=>e.title===I)??A[0],u[2]=I,u[3]=A,u[4]=s):s=u[4];let O=s;u[5]!==O||u[6]!==b||u[7]!==x?(o=e=>{let t=O?(0,v.getCategoryForTitle)(O.title):null,n=(0,v.getCategoryForTitle)(e.title);E(e.title),t!==n&&b.capture(l.PostHogEvent.ClickApiSdkCategory,{model:x,category:n}),b.capture(l.PostHogEvent.ClickApiSdkLanguage,{model:x,category:n,language:e.title})},u[5]=O,u[6]=b,u[7]=x,u[8]=o):o=u[8];let k=o;if(!O)return null;if(u[9]!==f?(r=(0,c.cn)("flex flex-col gap-2",f),u[9]=f,u[10]=r):r=u[10],u[11]!==O||u[12]!==k||u[13]!==A){let e;u[15]!==O||u[16]!==k?(e=e=>(0,t.jsx)(_.Button,{variant:"ghost",size:"xs",className:(0,c.cn)("h-auto shrink-0 px-2 py-1 text-xs leading-normal shadow-none",O===e?"bg-secondary font-medium text-accent-foreground":"text-muted-foreground hover:bg-transparent hover:text-accent-foreground"),onClick:()=>k(e),children:$[e.title]?.label??e.title},e.title),u[15]=O,u[16]=k,u[17]=e):e=u[17],i=A.map(e),u[11]=O,u[12]=k,u[13]=A,u[14]=i}else i=u[14];return u[18]!==i?(d=(0,t.jsx)("div",{className:"flex items-center gap-1 overflow-x-auto pb-1",children:i}),u[18]=i,u[19]=d):d=u[19],u[20]!==O.code||u[21]!==O.language?(p=(0,t.jsx)(j.ApiCodeBlock,{language:O.language,value:O.code}),u[20]=O.code,u[21]=O.language,u[22]=p):p=u[22],u[23]!==r||u[24]!==d||u[25]!==p?(m=(0,t.jsxs)("div",{className:r,children:[d,p]}),u[23]=r,u[24]=d,u[25]=p,u[26]=m):m=u[26],m}var E=e.i(78590),A=e.i(442427),O=e.i(860816),k=e.i(220988),w=e.i(364933);let R=[{role:"user",content:"Say hello in a friendly tone."}];var T=e.i(572729),S=A,N=w,C=A,q=w,F=e.i(274061);let L=[{role:"user",content:"Generate a beautiful sunset over mountains"}],K="Generate a beautiful sunset over mountains",z=({slug:e,provider:t,imageConfig:n,prompt:a=K})=>{let s=[{role:"user",content:a}],o=[n?`"image_config": ${(0,O.indentObjectParam)(n,16)}`:null,t?`"provider": ${(0,O.indentObjectParam)(t,16)}`:null].filter(e=>null!==e);return[{title:"@openrouter/sdk",language:"typescript",code:(0,O.normalizeIndentation)(`
import { OpenRouter } from "@openrouter/sdk";

const openrouter = new OpenRouter({
  apiKey: "${A.API_KEY_REF}"
});

const result = await openrouter.chat.send({
  model: "${e}",
  messages: [
    {
      role: "user",
      content: ${JSON.stringify(a)}
    }
  ],
  modalities: ["image"]${n?`,
  image_config: ${(0,O.indentObjectParam)(n,10)}`:""}${t?`,
  provider: ${(0,O.indentObjectParam)(t,10)}`:""}
});

const message = result.choices[0].message;
if (message.images) {
  message.images.forEach((image, index) => {
    const imageUrl = image.image_url.url;
    console.log(\`Generated image \${index + 1}: \${imageUrl.substring(0, 50)}...\`);
  });
}
      `,{baseIndent:8})},{title:"openai-python",language:"python",code:(0,O.normalizeIndentation)(`
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="${A.API_KEY_REF}",
)

# Generate an image
response = client.chat.completions.create(
  model="${e}",
  messages=${(0,O.indentObjectParam)(s,10)},
  extra_body=${(0,O.indentObjectParamPython)({...t?{provider:t}:{},modalities:["image"],...n?{image_config:n}:{}},10)}
)

# The generated image will be in the assistant message
response = response.choices[0].message
if response.images:
  for image in response.images:
    image_url = image['image_url']['url']  # Base64 data URL
    print(f"Generated image: {image_url[:50]}...")
      `,{baseIndent:8})},{title:"python",language:"python",code:`
        import requests
        import json

        response = requests.post(
          url="https://openrouter.ai/api/v1/chat/completions",
          headers={
            "Authorization": "Bearer ${A.API_KEY_REF}",
            "Content-Type": "application/json",
          },
          data=json.dumps({
            "model": "${e}",
            "messages": ${(0,O.indentObjectParam)(s,16)},
            "modalities": ["image"]${n?`,
            "image_config": ${(0,O.indentObjectParamPython)(n,16)}`:""}${t?`,
            "provider": ${(0,O.indentObjectParamPython)(t,16)}`:""}
          })
        )

        result = response.json()

        # The generated image will be in the assistant message
        if result.get("choices"):
          message = result["choices"][0]["message"]
          if message.get("images"):
            for image in message["images"]:
              image_url = image["image_url"]["url"]  # Base64 data URL
              print(f"Generated image: {image_url[:50]}...")
      `},{title:"typescript",language:"typescript",code:`
        const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
          method: 'POST',
          headers: {
            Authorization: \`Bearer \${${A.API_KEY_REF}}\`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: '${e}',
            messages: ${(0,O.indentObjectParam)(s,16)},
            modalities: ['image']${n?`,
            image_config: ${(0,O.indentObjectParam)(n,16)}`:""}${t?`,
            provider: ${(0,O.indentObjectParam)(t,16)}`:""}
          }),
        });

        const result = await response.json();

        if (result.choices) {
          const message = result.choices[0].message;
          if (message.images) {
            message.images.forEach((image, index) => {
              const imageUrl = image.image_url.url; // Base64 data URL
              console.log(\`Generated image \${index + 1}: \${imageUrl.substring(0, 50)}...\`);
            });
          }
        }
      `},{title:"openai-typescript",language:"typescript",code:`
        import OpenAI from 'openai';

        const client = new OpenAI({
          baseURL: 'https://openrouter.ai/api/v1',
          apiKey: '${A.API_KEY_REF}',
        });

        const apiResponse = await client.chat.completions.create({
          model: '${e}',
          messages: [
            {
              role: 'user' as const,
              content: ${JSON.stringify(a)},
            },
          ],
          modalities: ['image']${n?`,
          image_config: ${(0,O.indentObjectParam)(n,10)}`:""}${t?`,
          provider: ${(0,O.indentObjectParam)(t,10)}`:""}
        });

        const response = apiResponse.choices[0].message;
        if (response.images) {
          response.images.forEach((image, index) => {
            const imageUrl = image.image_url.url; // Base64 data URL
            console.log(\`Generated image \${index + 1}: \${imageUrl.substring(0, 50)}...\`);
          });
        }
      `},{title:"curl",language:"shell",code:(0,w.getCURLExample)({data:k.default`{
            "model": "${e}",
            "messages": ${(0,O.indentObjectParam)(s,16)},
            "modalities": ["image"]${o.length>0?`,
            ${o.join(",\n            ")}`:""}
        }`})}]},B="https://live.staticflickr.com/3851/14825276609_098cac593d_b.jpg";var H=A,U=e.i(517329);let Y="Are you sure? Think carefully.",D="https://live.staticflickr.com/3851/14825276609_098cac593d_b.jpg",M="Extract all text from this document image and return it as structured Markdown.",G=[{role:"user",content:[{type:"image_url",image_url:{url:D}},{type:"text",text:M}]}];var Q=A;let W=[{role:"user",content:"How many r's are in the word 'strawberry'?"}],J={aspect_ratio:"16:9",text_layout:[{text:"WANDER",bbox:[[.3,.1],[.7,.1],[.7,.2],[.3,.2]]}]},V={aspect_ratio:"16:9",rgb_colors:[[31,81,159],[217,138,78]],background_rgb_color:[245,240,230]},X="https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg",Z={font_inputs:[{font_url:"https://example.com/fonts/custom-font.ttf",text:"Hello World"}]};var ee=e.i(209232),et=e.i(186101);let en=(e,t)=>{switch(e){case r.QuickStartExampleType.AudioOutput:return(({slug:e,provider:t})=>[{title:"openai-python",language:"python",code:(0,O.normalizeIndentation)(`
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="${A.API_KEY_REF}",
)

# Audio output requires streaming
completion = client.chat.completions.create(
  model="${e}",
  messages=${(0,O.indentObjectParam)(R,4)},
  modalities=["text", "audio"],
  audio={"voice": "alloy", "format": "pcm16"},
  stream=True,
  extra_body=${t?(0,O.indentObjectParamPython)({provider:t},4):"{}"}
)

audio_data_chunks = []
transcript_chunks = []

for chunk in completion:
    delta = chunk.choices[0].delta
    if hasattr(delta, "audio") and delta.audio:
        if delta.audio.get("data"):
            audio_data_chunks.append(delta.audio["data"])
        if delta.audio.get("transcript"):
            transcript_chunks.append(delta.audio["transcript"])

transcript = "".join(transcript_chunks)
print(f"Transcript: {transcript}")

# Combine and decode the base64 audio chunks, then save
import base64
full_audio_b64 = "".join(audio_data_chunks)
audio_bytes = base64.b64decode(full_audio_b64)
with open("output.pcm", "wb") as f:
    f.write(audio_bytes)
      `,{baseIndent:8})},{title:"python",language:"python",code:`
        import requests
        import json
        import base64

        # Audio output requires streaming
        response = requests.post(
          url="https://openrouter.ai/api/v1/chat/completions",
          headers={
            "Authorization": "Bearer ${A.API_KEY_REF}",
            "Content-Type": "application/json",
          },
          data=json.dumps({
            "model": "${e}",
            "messages": ${(0,O.indentObjectParam)(R,16)},
            "modalities": ["text", "audio"],
            "audio": {
              "voice": "alloy",
              "format": "pcm16"
            },
            "stream": True${t?`,
            "provider": ${(0,O.indentObjectParamPython)(t,16)}`:""}
          }),
          stream=True
        )

        audio_data_chunks = []
        transcript_chunks = []

        for line in response.iter_lines():
            if not line:
                continue
            decoded = line.decode("utf-8")
            if not decoded.startswith("data: "):
                continue
            data = decoded[len("data: "):]
            if data.strip() == "[DONE]":
                break
            chunk = json.loads(data)
            delta = chunk["choices"][0].get("delta", {})
            audio = delta.get("audio", {})
            if audio.get("data"):
                audio_data_chunks.append(audio["data"])
            if audio.get("transcript"):
                transcript_chunks.append(audio["transcript"])

        transcript = "".join(transcript_chunks)
        print(f"Transcript: {transcript}")

        # Combine and decode the base64 audio chunks, then save
        full_audio_b64 = "".join(audio_data_chunks)
        audio_bytes = base64.b64decode(full_audio_b64)
        with open("output.pcm", "wb") as f:
            f.write(audio_bytes)
      `},{title:"typescript",language:"typescript",code:`
        // Audio output requires streaming
        const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
          method: "POST",
          headers: {
            "Authorization": \`Bearer \${${A.API_KEY_REF}}\`,
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            model: "${e}",
            messages: ${(0,O.indentObjectParam)(R,16)},
            modalities: ["text", "audio"],
            audio: {
              voice: "alloy",
              format: "pcm16"
            },
            stream: true${t?`,
            provider: ${(0,O.indentObjectParam)(t,16)}`:""}
          })
        });

        const reader = response.body!.getReader();
        const decoder = new TextDecoder();

        const audioDataChunks: string[] = [];
        const transcriptChunks: string[] = [];
        let buffer = "";

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });
          const lines = buffer.split("\\n");
          buffer = lines.pop()!;

          for (const line of lines) {
            if (!line.startsWith("data: ")) continue;
            const data = line.slice("data: ".length).trim();
            if (data === "[DONE]") break;

            const chunk = JSON.parse(data);
            const audio = chunk.choices?.[0]?.delta?.audio;
            if (audio?.data) audioDataChunks.push(audio.data);
            if (audio?.transcript) transcriptChunks.push(audio.transcript);
          }
        }

        const transcript = transcriptChunks.join("");
        console.log(\`Transcript: \${transcript}\`);

        // audioDataChunks joined together is the full base64-encoded audio
        const fullAudioB64 = audioDataChunks.join("");
      `},{title:"openai-typescript",language:"typescript",code:`
        import OpenAI from 'openai';

        const client = new OpenAI({
          baseURL: 'https://openrouter.ai/api/v1',
          apiKey: '${A.API_KEY_REF}',
        });

        // Audio output requires streaming
        const stream = await client.chat.completions.create({
          model: '${e}',
          messages: [
            {
              role: 'user' as const,
              content: 'Say hello in a friendly tone.',
            },
          ],
          modalities: ['text', 'audio'],
          audio: {
            voice: 'alloy',
            format: 'pcm16',
          },
          stream: true${t?`,
          provider: ${(0,O.indentObjectParam)(t,10)}`:""}
        });

        const audioDataChunks: string[] = [];
        const transcriptChunks: string[] = [];

        for await (const chunk of stream) {
          const delta = chunk.choices?.[0]?.delta;
          if (delta?.audio?.data) audioDataChunks.push(delta.audio.data);
          if (delta?.audio?.transcript) transcriptChunks.push(delta.audio.transcript);
        }

        const transcript = transcriptChunks.join("");
        console.log(\`Transcript: \${transcript}\`);

        // audioDataChunks joined together is the full base64-encoded audio
        const fullAudioB64 = audioDataChunks.join("");
      `},{title:"curl",language:"shell",code:(0,w.getCURLExample)({data:k.default`{
            "model": "${e}",
            "messages": ${(0,O.indentObjectParam)(R,16)},
            "modalities": ["text", "audio"],
            "audio": {
              "voice": "alloy",
              "format": "pcm16"
            },
            "stream": true${t?",":""}
            ${t?`"provider": ${(0,O.indentObjectParam)(t,16)}`:""}
        }`})}])(t);case r.QuickStartExampleType.Embeddings:return(({slug:e})=>[{title:"@openrouter/sdk",language:"typescript",code:(0,O.normalizeIndentation)(`
import { OpenRouter } from "@openrouter/sdk";

const openrouter = new OpenRouter({
  apiKey: "${S.API_KEY_REF}"
});

const embedding = await openrouter.embeddings.generate({
  requestBody: {
    model: "${e}",
    input: "Your text string goes here",
    encodingFormat: "float"
  }
});

console.log(embedding.data[0].embedding);
      `,{baseIndent:8})},{title:"openai-python",language:"python",code:(0,O.normalizeIndentation)(`
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="${S.API_KEY_REF}",
)

embedding = client.embeddings.create(
  extra_headers={
    ${(0,N.getHeaderLines)({commentPrefix:"#"}).join("\n    ")}
  },
  model="${e}",
  input="Your text string goes here",
  # input: ["text1", "text2", "text3"] # batch embeddings also supported!
  encoding_format="float"
)
print(embedding.data[0].embedding)
      `,{baseIndent:8})},{title:"python",language:"python",code:`
        import requests
        import json

        response = requests.post(
          url="https://openrouter.ai/api/v1/embeddings",
          headers={
            "Authorization": "Bearer ${S.API_KEY_REF}",
            "Content-Type": "application/json",
            ${(0,N.getHeaderLines)({commentPrefix:"#"}).join("\n            ")}
          },
          data=json.dumps({
            "model": "${e}",
            "input": "Your text string goes here",
            # "input": ["text1", "text2", "text3"], # batch embeddings also supported!
            "encoding_format": "float"
          })
        )
      `},{title:"typescript",language:"typescript",code:(({apiKey:e=S.API_KEY_REF,model:t,input:n="Your text string goes here",siteUrl:a=N.SITE_URL_REF,siteName:s=N.SITE_NAME_REF})=>`
  fetch("https://openrouter.ai/api/v1/embeddings", {
    method: "POST",
    headers: {
      "Authorization": \`Bearer \${${e}}\`,
      "Content-Type": "application/json",
      ${(0,N.getHeaderLines)({siteUrl:a,siteName:s}).join("\n      ")}
    },
    body: JSON.stringify({
      "model": "${t}",
      "input": "${n}",
      // "input": ["text1", "text2", "text3"], // batch embeddings also supported!
      "encoding_format": "float"
    })
  });
`)({model:e})},{title:"openai-typescript",language:"typescript",code:`
        import OpenAI from 'openai';

        const openai = new OpenAI({
          baseURL: "https://openrouter.ai/api/v1",
          apiKey: "${S.API_KEY_REF}",
          defaultHeaders: {
            ${(0,N.getHeaderLines)({}).join("\n            ")}
          },
        });

        async function main() {
          const embedding = await openai.embeddings.create({
            model: "${e}",
            input: "Your text string goes here",
            // input: ["text1", "text2", "text3"], // batch embeddings also supported!
            encoding_format: "float"
          });

          console.log(embedding.data[0].embedding);
        }

        main();
      `},{title:"curl",language:"shell",code:(({apiKey:e="$OPENROUTER_API_KEY",model:t,input:n="Your text string goes here"})=>(0,O.normalizeIndentation)(`
  # Note: "input" also supports batch processing with arrays: ["text1", "text2", "text3"]
  curl https://openrouter.ai/api/v1/embeddings \\
    -H "Authorization: Bearer ${e}" \\
    -H "Content-Type: application/json" \\
    -d '{
      "model": "${t}",
      "input": "${n}",
      "encoding_format": "float"
    }'
`,{baseIndent:8}))({model:e})}])(t);case r.QuickStartExampleType.ImageInputEmbeddings:return(({slug:e})=>[{title:"@openrouter/sdk",language:"typescript",code:(0,O.normalizeIndentation)(`
import { OpenRouter } from "@openrouter/sdk";

const openrouter = new OpenRouter({
  apiKey: "${A.API_KEY_REF}"
});

const embedding = await openrouter.embeddings.generate({
  requestBody: {
    model: "${e}",
    input: [
      {
        content: [
          { type: "text", text: "What is in this image?" },
          { type: "image_url", imageUrl: { url: "${B}" } }
        ]
      }
    ],
    encodingFormat: "float"
  }
});

console.log(embedding.data[0].embedding.slice(0, 5));
      `,{baseIndent:8})},{title:"openai-python",language:"python",code:(0,O.normalizeIndentation)(`
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="${A.API_KEY_REF}",
)

# Image input embeddings use multimodal content format
embedding = client.embeddings.create(
  extra_headers={
    ${(0,w.getHeaderLines)({commentPrefix:"#"}).join("\n    ")}
  },
  model="${e}",
  input=[
    {
      "content": [
        {"type": "text", "text": "What is in this image?"},
        {"type": "image_url", "image_url": {"url": "${B}"}}
      ]
    }
  ],
  encoding_format="float"
)

print(embedding.data[0].embedding[:5])
      `,{baseIndent:8})},{title:"python",language:"python",code:(0,O.normalizeIndentation)(`
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/embeddings",
  headers={
    "Authorization": "Bearer ${A.API_KEY_REF}",
    "Content-Type": "application/json",
    ${(0,w.getHeaderLines)({commentPrefix:"#"}).join("\n    ")}
  },
  data=json.dumps({
    "model": "${e}",
    "input": [
      {
        "content": [
          {"type": "text", "text": "What is in this image?"},
          {"type": "image_url", "image_url": {"url": "${B}"}}
        ]
      }
    ],
    "encoding_format": "float"
  })
)

print(response.json()["data"][0]["embedding"][:5])
      `,{baseIndent:8})},{title:"typescript",language:"typescript",code:(0,O.normalizeIndentation)(`
const response = await fetch("https://openrouter.ai/api/v1/embeddings", {
  method: "POST",
  headers: {
    "Authorization": \`Bearer \${${A.API_KEY_REF}}\`,
    "Content-Type": "application/json",
    ${(0,w.getHeaderLines)({}).join("\n    ")}
  },
  body: JSON.stringify({
    "model": "${e}",
    "input": [
      {
        "content": [
          { "type": "text", "text": "What is in this image?" },
          { "type": "image_url", "image_url": { "url": "${B}" } }
        ]
      }
    ],
    "encoding_format": "float"
  })
});

const data = await response.json();
console.log(data.data[0].embedding.slice(0, 5));
      `,{baseIndent:8})},{title:"openai-typescript",language:"typescript",code:(0,O.normalizeIndentation)(`
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: "${A.API_KEY_REF}",
  defaultHeaders: {
    ${(0,w.getHeaderLines)({}).join("\n    ")}
  },
});

async function main() {
  // Image input embeddings use multimodal content format
  const embedding = await openai.embeddings.create({
    model: "${e}",
    input: [
      {
        content: [
          { type: "text", text: "What is in this image?" },
          { type: "image_url", image_url: { url: "${B}" } }
        ]
      }
    ] as unknown as string[],
    encoding_format: "float"
  });

  console.log(embedding.data[0].embedding.slice(0, 5));
}

main();
      `,{baseIndent:8})},{title:"curl",language:"shell",code:(0,O.normalizeIndentation)(`
curl https://openrouter.ai/api/v1/embeddings \\
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "${e}",
    "input": [
      {
        "content": [
          {"type": "text", "text": "What is in this image?"},
          {"type": "image_url", "image_url": {"url": "${B}"}}
        ]
      }
    ],
    "encoding_format": "float"
  }'
      `,{baseIndent:8})}])(t);case r.QuickStartExampleType.FastApply:return(({slug:e})=>[{title:"@openrouter/sdk",language:"typescript",code:(0,O.normalizeIndentation)(`
import { OpenRouter } from "@openrouter/sdk";

const openrouter = new OpenRouter({
  apiKey: "${C.API_KEY_REF}"
});

const result = await openrouter.chat.send({
  model: "${e}",
  messages: [
    {
      role: "user",
      content: \`<instruction>I will add type hints</instruction>
<code>def greet(name):
    return "Hello " + name</code>
<update>def greet(name: str) -> str:
// ...existing code...</update>\`
    }
  ]
});

console.log(result.choices[0].message.content);
      `,{baseIndent:8})},{title:"openai-python",language:"python",code:(({apiKey:e=C.API_KEY_REF,model:t,initialCode:n='def greet(name):\\n    return "Hello " + name',codeEdit:a="def greet(name: str) -> str:",instructions:s="I will add type hints"})=>(0,O.normalizeIndentation)(`
from openai import OpenAI

# Initialize client
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="${e}",
)

# Sample data
initial_code = """${n.replaceAll("\\n","\n")}"""

code_edit = """${a.replaceAll("\\n","\n")}"""

instructions = "${s}"

# Apply the edit
response = client.chat.completions.create(
  extra_headers={
    ${(0,q.getHeaderLines)({commentPrefix:"#"}).join("\n    ")}
  },
  model="${t}",
  messages=[
    {
      "role": "user",
      "content": f"<instruction>{instructions}</instruction>\\n<code>{initial_code}</code>\\n<update>{code_edit}</update>"
    }
  ]
)

merged_code = response.choices[0].message.content
print(merged_code)
    `,{baseIndent:8}))({model:e})},{title:"python",language:"python",code:(({apiKey:e=C.API_KEY_REF,model:t,initialCode:n='def greet(name):\\n    return "Hello " + name',codeEdit:a="def greet(name: str) -> str",instructions:s="I will add type hints"})=>(0,O.normalizeIndentation)(`
import requests
import json

# Sample data
initial_code = """${n.replaceAll("\\n","\n")}"""

code_edit = """${a.replaceAll("\\n","\n")}"""

instructions = "${s}"

# Apply the edit
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer ${e}",
    "Content-Type": "application/json",
    ${(0,q.getHeaderLines)({commentPrefix:"#"}).join("\n    ")}
  },
  data=json.dumps({
    "model": "${t}",
    "messages": [
      {
        "role": "user",
        "content": f"<instruction>{instructions}</instruction>\\n<code>{initial_code}</code>\\n<update>{code_edit}</update>"
      }
    ]
  })
)

merged_code = response.json()["choices"][0]["message"]["content"]
print(merged_code)
    `,{baseIndent:8}))({model:e})},{title:"typescript",language:"typescript",code:(({apiKey:e=C.API_KEY_REF,model:t,initialCode:n='def greet(name):\\n    return "Hello " + name',codeEdit:a="def greet(name: str) -> str:\\n// ...existing code...",instructions:s="I will add type hints",siteUrl:o=q.SITE_URL_REF,siteName:r=q.SITE_NAME_REF})=>`
  // Sample data
  const initialCode = \`${n.replaceAll("\\n","\n")}\`;

  const codeEdit = \`${a.replaceAll("\\n","\n")}\`;

  const instructions = \`${s}\`;

  // Apply the edit
  fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": \`Bearer \${${e}}\`,
      "Content-Type": "application/json",
      ${(0,q.getHeaderLines)({siteUrl:o,siteName:r}).join("\n      ")}
    },
    body: JSON.stringify({
      "model": "${t}",
      "messages": [
        {
          "role": "user",
          "content": \`<instruction>\${instructions}</instruction>\\n<code>\${initialCode}</code>\\n<update>\${codeEdit}</update>\`
        }
      ]
    })
  });
`)({model:e})},{title:"openai-typescript",language:"typescript",code:(({apiKey:e=C.API_KEY_REF,model:t,initialCode:n="def greet(name):\\n    return 'Hello' + name",codeEdit:a="def greet(name: str) -> str:",instructions:s="I will add type hints"})=>(0,O.normalizeIndentation)(`import OpenAI from 'openai';

// Initialize client
const openai = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: "${e}",
  defaultHeaders: {
    ${(0,q.getHeaderLines)({}).join("\n    ")}
  },
});

// Sample data
const initialCode = "${n.replaceAll("\\n","\\n")}";

const codeEdit = "${a.replaceAll("\\n","\\n")}";

const instructions = "${s}";

// Apply the edit
async function main() {
  const completion = await openai.chat.completions.create({
    model: "${t}",
    messages: [
      {
        role: "user",
        content: \`<instruction>\${instructions}</instruction>\\n<code>\${initialCode}</code>\\n<update>\${codeEdit}</update>\`
      }
    ]
  });

  const mergedCode = completion.choices[0].message.content;
  console.log(mergedCode);
}

main();
`,{baseIndent:8}))({model:e})},{title:"curl",language:"shell",code:(({apiKey:e="$OPENROUTER_API_KEY",model:t,initialCode:n="def greet(name):\\n    return `Hello` + name",codeEdit:a="def greet(name: str) -> str:\\n// ...existing code...",instructions:s="I will add type hints"})=>(0,O.normalizeIndentation)(`
  curl https://openrouter.ai/api/v1/chat/completions \\
    -H "Authorization: Bearer ${e}" \\
    -H "Content-Type: application/json" \\
    -d '{
      "model": "${t}",
      "messages": [
        {
          "role": "user",
          "content": "<instruction>${s}</instruction>\\n<code>${n}</code>\\n<update>${a}</update>"
        }
      ]
    }'
`,{baseIndent:8}))({model:e})}])(t);case r.QuickStartExampleType.Reasoning:return t.slug.startsWith("meta/")?(({slug:e,inputModalities:t,provider:n})=>[{title:"@openrouter/sdk",language:"typescript",code:(0,O.normalizeIndentation)(`
import { OpenRouter } from "@openrouter/sdk";

const openrouter = new OpenRouter({
  apiKey: "${H.API_KEY_REF}"
});

// Reasoning shares the output budget with the answer, so
// reserve room (>= ~2000 tokens) for reliable visible text
const stream = await openrouter.chat.send({
  chatRequest: {
    model: "${e}",
    messages: ${(0,U.getSdkMessagesExample)(t,6)},
    reasoning: { effort: "medium" },
    maxCompletionTokens: 2000,
    stream: true${n?`,
    provider: ${(0,O.indentObjectParam)(n,12)}`:""}
  }
});

let response = "";
for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) {
    response += content;
    process.stdout.write(content);
  }

  // Usage information comes in the final chunk
  if (chunk.usage) {
    console.log("\\nReasoning tokens:", chunk.usage.completionTokensDetails?.reasoningTokens);
  }
}
      `,{baseIndent:8})},{title:"openai-python",language:"python",code:(0,O.normalizeIndentation)(`
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="${H.API_KEY_REF}",
)

messages = ${(0,U.getMessagesExample)(t,2)}

# First API call. Reasoning shares the output budget with the
# answer, so reserve room (>= ~2000 tokens) for visible text
response = client.chat.completions.create(
  model="${e}",
  messages=messages,
  max_tokens=2000,
  extra_body=${n?(0,O.indentObjectParamPython)({provider:n,reasoning:{effort:"medium"}},10):'{"reasoning": {"effort": "medium"}}'}
)

# Extract the assistant message with reasoning_details
# (the model's reasoning comes back as an encrypted blob)
reply = response.choices[0].message

# Preserve the assistant message with reasoning_details
messages += [
  {
    "role": "assistant",
    "content": reply.content,
    "reasoning_details": reply.reasoning_details  # Pass back unmodified
  },
  {"role": "user", "content": "${Y}"}
]

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="${e}",
  messages=messages,
  max_tokens=2000,
  extra_body=${n?(0,O.indentObjectParamPython)({provider:n,reasoning:{effort:"medium"}},10):'{"reasoning": {"effort": "medium"}}'}
)
      `,{baseIndent:8})},{title:"python",language:"python",code:`
        import requests
        import json

        messages = ${(0,U.getMessagesExample)(t,8)}

        # First API call. Reasoning shares the output budget with the
        # answer, so reserve room (>= ~2000 tokens) for visible text
        response = requests.post(
          url="https://openrouter.ai/api/v1/chat/completions",
          headers={
            "Authorization": "Bearer ${H.API_KEY_REF}",
            "Content-Type": "application/json",
          },
          data=json.dumps({
            "model": "${e}",
            "messages": messages,
            "max_tokens": 2000,
            "reasoning": {"effort": "medium"}${n?`,
            "provider": ${(0,O.indentObjectParamPython)(n,16)}`:""}
          })
        )

        # Extract the assistant message with reasoning_details
        # (the model's reasoning comes back as an encrypted blob)
        reply = response.json()['choices'][0]['message']

        # Preserve the assistant message with reasoning_details
        messages += [
          {
            "role": "assistant",
            "content": reply.get('content'),
            "reasoning_details": reply.get('reasoning_details')  # Pass back unmodified
          },
          {"role": "user", "content": "${Y}"}
        ]

        # Second API call - model continues reasoning from where it left off
        response2 = requests.post(
          url="https://openrouter.ai/api/v1/chat/completions",
          headers={
            "Authorization": "Bearer ${H.API_KEY_REF}",
            "Content-Type": "application/json",
          },
          data=json.dumps({
            "model": "${e}",
            "messages": messages,  # Includes preserved reasoning_details
            "max_tokens": 2000,
            "reasoning": {"effort": "medium"}${n?`,
            "provider": ${(0,O.indentObjectParamPython)(n,16)}`:""}
          })
        )
      `},{title:"typescript",language:"typescript",code:(({apiKey:e=H.API_KEY_REF,model:t,messages:n,provider:a})=>`
  const messages = ${n};

  // First API call. Reasoning shares the output budget with the
  // answer, so reserve room (>= ~2000 tokens) for visible text
  const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": "Bearer ${e}",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      "model": "${t}",
      "messages": messages,
      "max_tokens": 2000,
      "reasoning": {"effort": "medium"}${a?`,
      "provider": ${(0,O.indentObjectParam)(a,6)}`:""}
    })
  });

  // Extract the assistant message with reasoning_details
  // (the model's reasoning comes back as an encrypted blob)
  const result = await response.json();
  const reply = result.choices[0].message;

  // Preserve the assistant message with reasoning_details
  messages.push(
    {
      role: 'assistant',
      content: reply.content,
      reasoning_details: reply.reasoning_details, // Pass back unmodified
    },
    {
      role: 'user',
      content: '${Y}',
    },
  );

  // Second API call - model continues reasoning from where it left off
  const response2 = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": "Bearer ${e}",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      "model": "${t}",
      "messages": messages,  // Includes preserved reasoning_details
      "max_tokens": 2000,
      "reasoning": {"effort": "medium"}${a?`,
      "provider": ${(0,O.indentObjectParam)(a,6)}`:""}
    })
  });
`)({model:e,messages:(0,U.getMessagesExample)(t,2),provider:n})},{title:"openai-typescript",language:"typescript",code:`
        import OpenAI from 'openai';

        const client = new OpenAI({
          baseURL: 'https://openrouter.ai/api/v1',
          apiKey: '${H.API_KEY_REF}',
        });

        const messages = ${(0,U.getMessagesExample)(t,8)};

        // First API call. Reasoning shares the output budget with the
        // answer, so reserve room (>= ~2000 tokens) for visible text
        const apiResponse = await client.chat.completions.create({
          model: '${e}',
          messages,
          max_tokens: 2000,
          reasoning: { effort: 'medium' }${n?`,
          provider: ${(0,O.indentObjectParam)(n,10)}`:""}
        });

        // Extract the assistant message with reasoning_details
        // (the model's reasoning comes back as an encrypted blob)
        type ORChatMessage = (typeof apiResponse)['choices'][number]['message'] & {
          reasoning_details?: unknown;
        };
        const reply = apiResponse.choices[0].message as ORChatMessage;

        // Preserve the assistant message with reasoning_details
        messages.push(
          {
            role: 'assistant',
            content: reply.content,
            reasoning_details: reply.reasoning_details, // Pass back unmodified
          },
          {
            role: 'user',
            content: '${Y}',
          },
        );

        // Second API call - model continues reasoning from where it left off
        const response2 = await client.chat.completions.create({
          model: '${e}',
          messages, // Includes preserved reasoning_details
          max_tokens: 2000,
          reasoning: { effort: 'medium' }${n?`,
          provider: ${(0,O.indentObjectParam)(n,10)}`:""}
        });
      `},{title:"curl",language:"shell",code:(({apiKey:e="$OPENROUTER_API_KEY",model:t,messages:n,provider:a})=>(0,w.getCURLExample)({apiKey:e,data:k.default`{
            "model": "${t}",
            "messages": ${n},
            "max_tokens": ${2e3},
            "reasoning": {
              "effort": "medium"
            }${a?`,
  "provider": ${(0,O.indentObjectParam)(a,2)}`:""}
        }`}))({model:e,messages:(0,U.getMessagesExample)(t,12),provider:n})}])(t):(({slug:e,provider:t})=>[{title:"@openrouter/sdk",language:"typescript",code:(0,O.normalizeIndentation)(`
import { OpenRouter } from "@openrouter/sdk";

const openrouter = new OpenRouter({
  apiKey: "${Q.API_KEY_REF}"
});

// Stream the response to get reasoning tokens in usage
const stream = await openrouter.chat.send({
  chatRequest: {
    model: "${e}",
    messages: [
      {
        role: "user",
        content: "How many r's are in the word 'strawberry'?"
      }
    ],
    stream: true${t?`,
    provider: ${(0,O.indentObjectParam)(t,12)}`:""}
  }
});

let response = "";
for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) {
    response += content;
    process.stdout.write(content);
  }

  // Usage information comes in the final chunk
  if (chunk.usage) {
    console.log("\\nReasoning tokens:", chunk.usage.completionTokensDetails?.reasoningTokens);
  }
}
      `,{baseIndent:8})},{title:"openai-python",language:"python",code:(0,O.normalizeIndentation)(`
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="${Q.API_KEY_REF}",
)

# First API call with reasoning
response = client.chat.completions.create(
  model="${e}",
  messages=${(0,O.indentObjectParam)(W,10)},
  extra_body=${t?(0,O.indentObjectParamPython)({provider:t,reasoning:{enabled:!0}},10):'{"reasoning": {"enabled": True}}'}
)

# Extract the assistant message with reasoning_details
response = response.choices[0].message

# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
  {
    "role": "assistant",
    "content": response.content,
    "reasoning_details": response.reasoning_details  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="${e}",
  messages=messages,
  extra_body=${t?(0,O.indentObjectParamPython)({provider:t,reasoning:{enabled:!0}},10):'{"reasoning": {"enabled": True}}'}
)
      `,{baseIndent:8})},{title:"python",language:"python",code:`
        import requests
        import json

        # First API call with reasoning
        response = requests.post(
          url="https://openrouter.ai/api/v1/chat/completions",
          headers={
            "Authorization": "Bearer ${Q.API_KEY_REF}",
            "Content-Type": "application/json",
          },
          data=json.dumps({
            "model": "${e}",
            "messages": ${(0,O.indentObjectParam)(W,16)},
            "reasoning": {"enabled": True}${t?`,
            "provider": ${(0,O.indentObjectParamPython)(t,16)}`:""}
          })
        )

        # Extract the assistant message with reasoning_details
        response = response.json()
        response = response['choices'][0]['message']

        # Preserve the assistant message with reasoning_details
        messages = [
          {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
          {
            "role": "assistant",
            "content": response.get('content'),
            "reasoning_details": response.get('reasoning_details')  # Pass back unmodified
          },
          {"role": "user", "content": "Are you sure? Think carefully."}
        ]

        # Second API call - model continues reasoning from where it left off
        response2 = requests.post(
          url="https://openrouter.ai/api/v1/chat/completions",
          data=json.dumps({
            "model": "${e}",
            "messages": messages,  # Includes preserved reasoning_details
            "reasoning": {"enabled": True}${t?`,
            "provider": ${(0,O.indentObjectParamPython)(t,16)}`:""}
          })
        )
      `},{title:"typescript",language:"typescript",code:(({apiKey:e=Q.API_KEY_REF,model:t,messages:n,provider:a})=>`
  // First API call with reasoning
  let response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": \`Bearer \${${e}}\`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      "model": "${t}",
      "messages": ${n},
      "reasoning": {"enabled": true}${a?`,
      "provider": ${(0,O.indentObjectParam)(a,6)}`:""}
    })
  });

  // Extract the assistant message with reasoning_details and save it to the response variable
  const result = await response.json();
  response = result.choices[0].message;

  // Preserve the assistant message with reasoning_details
  const messages = [
    {
      role: 'user',
      content: "How many r's are in the word 'strawberry'?",
    },
    {
      role: 'assistant',
      content: response.content,
      reasoning_details: response.reasoning_details, // Pass back unmodified
    },
    {
      role: 'user',
      content: "Are you sure? Think carefully.",
    },
  ];

  // Second API call - model continues reasoning from where it left off
  const response2 = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": \`Bearer \${${e}}\`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      "model": "${t}",
      "messages": messages${a?`,  // Includes preserved reasoning_details
      "provider": ${(0,O.indentObjectParam)(a,6)}`:"  // Includes preserved reasoning_details"}
    })
  });
`)({model:e,messages:(0,O.indentObjectParam)(W,8),provider:t})},{title:"openai-typescript",language:"typescript",code:`
        import OpenAI from 'openai';

        const client = new OpenAI({
          baseURL: 'https://openrouter.ai/api/v1',
          apiKey: '${Q.API_KEY_REF}',
        });

        // First API call with reasoning
        const apiResponse = await client.chat.completions.create({
          model: '${e}',
          messages: [
            {
              role: 'user' as const,
              content: "How many r's are in the word 'strawberry'?",
            },
          ],
          reasoning: { enabled: true }${t?`,
          provider: ${(0,O.indentObjectParam)(t,10)}`:""}
        });

        // Extract the assistant message with reasoning_details
        type ORChatMessage = (typeof apiResponse)['choices'][number]['message'] & {
          reasoning_details?: unknown;
        };
        const response = apiResponse.choices[0].message as ORChatMessage;

        // Preserve the assistant message with reasoning_details
        const messages = [
          {
            role: 'user' as const,
            content: "How many r's are in the word 'strawberry'?",
          },
          {
            role: 'assistant' as const,
            content: response.content,
            reasoning_details: response.reasoning_details, // Pass back unmodified
          },
          {
            role: 'user' as const,
            content: "Are you sure? Think carefully.",
          },
        ];

        // Second API call - model continues reasoning from where it left off
        const response2 = await client.chat.completions.create({
          model: '${e}',
          messages,${t?`, // Includes preserved reasoning_details
          provider: ${(0,O.indentObjectParam)(t,10)}`:" // Includes preserved reasoning_details"}
        });
      `},{title:"curl",language:"shell",code:(({apiKey:e="$OPENROUTER_API_KEY",model:t,provider:n})=>(0,w.getCURLExample)({apiKey:e,data:k.default`{
            "model": "${t}",
            "messages": [
              {
                "role": "user",
                "content": "How many r\`s are in the word \`strawberry?\`"
              }
            ],
            "reasoning": {
              "enabled": true
            }${n?",":""}
        }`}))({model:e,provider:t})}])(t);case r.QuickStartExampleType.ImageGeneration:return(({slug:e,provider:t})=>[{title:"@openrouter/sdk",language:"typescript",code:(0,O.normalizeIndentation)(`
import { OpenRouter } from "@openrouter/sdk";

const openrouter = new OpenRouter({
  apiKey: "${A.API_KEY_REF}"
});

const result = await openrouter.chat.send({
  model: "${e}",
  messages: [
    {
      role: "user",
      content: "Generate a beautiful sunset over mountains"
    }
  ],
  modalities: ["image", "text"]${t?`,
  provider: ${(0,O.indentObjectParam)(t,10)}`:""}
});

const message = result.choices[0].message;
if (message.images) {
  message.images.forEach((image, index) => {
    const imageUrl = image.image_url.url;
    console.log(\`Generated image \${index + 1}: \${imageUrl.substring(0, 50)}...\`);
  });
}
      `,{baseIndent:8})},{title:"openai-python",language:"python",code:(0,O.normalizeIndentation)(`
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="${A.API_KEY_REF}",
)

# Generate an image
response = client.chat.completions.create(
  model="${e}",
  messages=${(0,O.indentObjectParam)(L,10)},
  extra_body=${t?(0,O.indentObjectParamPython)({provider:t,modalities:["image","text"]},10):'{"modalities": ["image", "text"]}'}
)

# The generated image will be in the assistant message
response = response.choices[0].message
if response.images:
  for image in response.images:
    image_url = image['image_url']['url']  # Base64 data URL
    print(f"Generated image: {image_url[:50]}...")
      `,{baseIndent:8})},{title:"python",language:"python",code:`
        import requests
        import json

        response = requests.post(
          url="https://openrouter.ai/api/v1/chat/completions",
          headers={
            "Authorization": "Bearer ${A.API_KEY_REF}",
            "Content-Type": "application/json",
          },
          data=json.dumps({
            "model": "${e}",
            "messages": ${(0,O.indentObjectParam)(L,16)},
            "modalities": ["image", "text"]${t?`,
            "provider": ${(0,O.indentObjectParamPython)(t,16)}`:""}
          })
        )

        result = response.json()

        # The generated image will be in the assistant message
        if result.get("choices"):
          message = result["choices"][0]["message"]
          if message.get("images"):
            for image in message["images"]:
              image_url = image["image_url"]["url"]  # Base64 data URL
              print(f"Generated image: {image_url[:50]}...")
      `},{title:"typescript",language:"typescript",code:`
        const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
          method: 'POST',
          headers: {
            Authorization: \`Bearer \${${A.API_KEY_REF}}\`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: '${e}',
            messages: ${(0,O.indentObjectParam)(L,16)},
            modalities: ['image', 'text']${t?`,
            provider: ${(0,O.indentObjectParam)(t,16)}`:""}
          }),
        });

        const result = await response.json();

        if (result.choices) {
          const message = result.choices[0].message;
          if (message.images) {
            message.images.forEach((image, index) => {
              const imageUrl = image.image_url.url; // Base64 data URL
              console.log(\`Generated image \${index + 1}: \${imageUrl.substring(0, 50)}...\`);
            });
          }
        }
      `},{title:"openai-typescript",language:"typescript",code:`
        import OpenAI from 'openai';

        const client = new OpenAI({
          baseURL: 'https://openrouter.ai/api/v1',
          apiKey: '${A.API_KEY_REF}',
        });

        const apiResponse = await client.chat.completions.create({
          model: '${e}',
          messages: [
            {
              role: 'user' as const,
              content: 'Generate a beautiful sunset over mountains',
            },
          ],
          modalities: ['image', 'text']${t?`,
          provider: ${(0,O.indentObjectParam)(t,10)}`:""}
        });

        const response = apiResponse.choices[0].message;
        if (response.images) {
          response.images.forEach((image, index) => {
            const imageUrl = image.image_url.url; // Base64 data URL
            console.log(\`Generated image \${index + 1}: \${imageUrl.substring(0, 50)}...\`);
          });
        }
      `},{title:"curl",language:"shell",code:(0,w.getCURLExample)({data:k.default`{
            "model": "${e}",
            "messages": ${(0,O.indentObjectParam)(L,16)},
            "modalities": ["image", "text"]${t?",":""}
            ${t?`"provider": ${(0,O.indentObjectParam)(t,16)}`:""}
        }`})}])(t);case r.QuickStartExampleType.ImageGenerationWithoutText:return t.slug.startsWith("recraft/recraft-v3")?(({slug:e,provider:t})=>z({slug:e,provider:t,prompt:'A serene mountain lake at sunset with the headline "WANDER" across the top',imageConfig:J}))(t):t.slug.startsWith("recraft/recraft-v4")?(({slug:e,provider:t})=>z({slug:e,provider:t,prompt:"A minimalist abstract poster of mountains and clouds",imageConfig:V}))(t):t.slug.startsWith("sourceful/")?(({slug:e,provider:t})=>z({slug:e,provider:t,prompt:'A vibrant billboard in a bustling city with the headline "Hello World"',imageConfig:Z}))(t):(({slug:e,provider:t})=>z({slug:e,provider:t}))(t);case r.QuickStartExampleType.VideoGeneration:return t.slug.startsWith("x-ai/grok-imagine-video-1.5")?(({slug:e})=>(0,F.buildVideoGenerationExamples)({slug:e,prompt:"The dolphins leap out of the water in a graceful arc, sunlight glinting off the waves",requestFields:{frame_images:[{type:"image_url",image_url:{url:"https://live.staticflickr.com/3851/14825276609_098cac593d_b.jpg"},frame_type:"first_frame"}],resolution:"1080p"}}))(t):t.slug.startsWith("heygen/avatar-iv")?(({slug:e})=>(0,F.buildVideoGenerationExamples)({slug:e,prompt:"Welcome to our product tour! In the next two minutes I will show you the three features our customers love most.",requestFields:{input_references:[{type:"image_url",image_url:{url:"https://images.unsplash.com/photo-1772371272208-412168748f2a?w=800"}}],provider:{options:{heygen:{voice_id:"f38a635bee7a4d1f9b0a654a31d050d2"}}}}}))(t):t.slug.startsWith("heygen/video-agent")?(({slug:e})=>(0,F.buildVideoGenerationExamples)({slug:e,prompt:"Create a 60-second explainer video announcing our new mobile app. Cover the three headline features, keep the tone upbeat, and end with a call to action to download it."}))(t):(0,F.getVideoGenerationExamples)(t);case r.QuickStartExampleType.Rerank:return t.inputModalities.includes(o.InputModality.Image)?(({slug:e})=>[{title:"python",language:"python",code:(0,O.normalizeIndentation)(`
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/rerank",
  headers={
    "Authorization": "Bearer ${A.API_KEY_REF}",
    "Content-Type": "application/json",
    ${(0,w.getHeaderLines)({commentPrefix:"#"}).join("\n    ")}
  },
  data=json.dumps({
    "model": "${e}",
    "query": "a photograph of a cat",
    # Documents can mix images and text. Images are remote URLs or base64 data URIs.
    "documents": [
      {"image": "${X}"},
      {"text": "A fluffy cat sitting on a windowsill in the sun."},
      {"text": "A street map of downtown Berlin."}
    ],
    "top_n": 3
  })
)

results = response.json()
for result in results["results"]:
  document = result["document"]
  source = document.get("image") or document.get("text")
  print(f"Index: {result['index']}, Score: {result['relevance_score']}, Source: {source}")
      `,{baseIndent:8})},{title:"typescript",language:"typescript",code:`
        const response = await fetch("https://openrouter.ai/api/v1/rerank", {
          method: "POST",
          headers: {
            "Authorization": \`Bearer \${${A.API_KEY_REF}}\`,
            "Content-Type": "application/json",
            ${(0,w.getHeaderLines)({siteUrl:w.SITE_URL_REF,siteName:w.SITE_NAME_REF}).join("\n            ")}
          },
          body: JSON.stringify({
            model: "${e}",
            query: "a photograph of a cat",
            // Documents can mix images and text. Images are remote URLs or base64 data URIs.
            documents: [
              { image: "${X}" },
              { text: "A fluffy cat sitting on a windowsill in the sun." },
              { text: "A street map of downtown Berlin." }
            ],
            top_n: 3
          })
        });

        const data = await response.json();
        for (const result of data.results) {
          const source = result.document.image ?? result.document.text;
          console.log(\`Index: \${result.index}, Score: \${result.relevance_score}, Source: \${source}\`);
        }
      `},{title:"curl",language:"shell",code:k.default`
        curl https://openrouter.ai/api/v1/rerank \\
          -H "Content-Type: application/json" \\
          -H "Authorization: Bearer $OPENROUTER_API_KEY" \\
          -d '{
            "model": "${e}",
            "query": "a photograph of a cat",
            "documents": [
              {"image": "${X}"},
              {"text": "A fluffy cat sitting on a windowsill in the sun."},
              {"text": "A street map of downtown Berlin."}
            ],
            "top_n": 3
          }'
      `}])(t):(({slug:e})=>[{title:"python",language:"python",code:(0,O.normalizeIndentation)(`
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/rerank",
  headers={
    "Authorization": "Bearer ${A.API_KEY_REF}",
    "Content-Type": "application/json",
    ${(0,w.getHeaderLines)({commentPrefix:"#"}).join("\n    ")}
  },
  data=json.dumps({
    "model": "${e}",
    "query": "What is the capital of France?",
    "documents": [
      "Paris is the capital of France.",
      "London is the capital of England.",
      "Berlin is the capital of Germany."
    ],
    "top_n": 3
  })
)

results = response.json()
for result in results["results"]:
  print(f"Index: {result['index']}, Score: {result['relevance_score']}")
  print(f"  Document: {result['document']['text']}")
      `,{baseIndent:8})},{title:"typescript",language:"typescript",code:`
        const response = await fetch("https://openrouter.ai/api/v1/rerank", {
          method: "POST",
          headers: {
            "Authorization": \`Bearer \${${A.API_KEY_REF}}\`,
            "Content-Type": "application/json",
            ${(0,w.getHeaderLines)({siteUrl:w.SITE_URL_REF,siteName:w.SITE_NAME_REF}).join("\n            ")}
          },
          body: JSON.stringify({
            model: "${e}",
            query: "What is the capital of France?",
            documents: [
              "Paris is the capital of France.",
              "London is the capital of England.",
              "Berlin is the capital of Germany."
            ],
            top_n: 3
          })
        });

        const data = await response.json();
        for (const result of data.results) {
          console.log(\`Index: \${result.index}, Score: \${result.relevance_score}\`);
          console.log(\`  Document: \${result.document.text}\`);
        }
      `},{title:"curl",language:"shell",code:k.default`
        curl https://openrouter.ai/api/v1/rerank \\
          -H "Content-Type: application/json" \\
          -H "Authorization: Bearer $OPENROUTER_API_KEY" \\
          -d '{
            "model": "${e}",
            "query": "What is the capital of France?",
            "documents": [
              "Paris is the capital of France.",
              "London is the capital of England.",
              "Berlin is the capital of Germany."
            ],
            "top_n": 3
          }'
      `}])(t);case r.QuickStartExampleType.TTS:return(0,et.getTtsExamples)(t);case r.QuickStartExampleType.STT:return(0,ee.getSttExamples)(t);case r.QuickStartExampleType.OCR:return(({slug:e,provider:t})=>[{title:"@openrouter/sdk",language:"typescript",code:(0,O.normalizeIndentation)(`
import { OpenRouter } from "@openrouter/sdk";

const openrouter = new OpenRouter({
  apiKey: "${A.API_KEY_REF}"
});

const result = await openrouter.chat.send({
  model: "${e}",
  messages: [
    {
      role: "user",
      content: [
        {
          type: "image_url",
          image_url: {
            url: "${D}"
          }
        },
        {
          type: "text",
          text: "${M}"
        }
      ]
    }
  ]${t?`,
  provider: ${(0,O.indentObjectParam)(t,2)}`:""}
});

console.log(result.choices[0].message.content);
      `,{baseIndent:8})},{title:"openai-python",language:"python",code:(0,O.normalizeIndentation)(`
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="${A.API_KEY_REF}",
)

response = client.chat.completions.create(
  model="${e}",
  messages=${(0,O.indentObjectParam)(G,2)}${t?`,
  extra_body=${(0,O.indentObjectParamPython)({provider:t},2)}`:""}
)

print(response.choices[0].message.content)
      `,{baseIndent:8})},{title:"python",language:"python",code:(0,O.normalizeIndentation)(`
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer ${A.API_KEY_REF}",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "${e}",
    "messages": ${(0,O.indentObjectParamPython)(G,4)}${t?`,
    "provider": ${(0,O.indentObjectParamPython)(t,4)}`:""}
  })
)

result = response.json()
print(result["choices"][0]["message"]["content"])
      `,{baseIndent:8})},{title:"typescript",language:"typescript",code:(0,O.normalizeIndentation)(`
const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
  method: "POST",
  headers: {
    "Authorization": \`Bearer \${${A.API_KEY_REF}}\`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "${e}",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "image_url",
            image_url: {
              url: "${D}"
            }
          },
          {
            type: "text",
            text: "${M}"
          }
        ]
      }
    ]${t?`,
    provider: ${(0,O.indentObjectParam)(t,4)}`:""}
  }),
});

const result = await response.json();
console.log(result.choices[0].message.content);
      `,{baseIndent:8})},{title:"openai-typescript",language:"typescript",code:(0,O.normalizeIndentation)(`
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: "${A.API_KEY_REF}",
  defaultHeaders: {
    ${(0,w.getHeaderLines)({}).join("\n    ")}
  },
});

const response = await client.chat.completions.create({
  model: "${e}",
  messages: [
    {
      role: "user",
      content: [
        {
          type: "image_url",
          image_url: {
            url: "${D}"
          }
        },
        {
          type: "text",
          text: "${M}"
        }
      ]
    }
  ]${t?`,
  provider: ${(0,O.indentObjectParam)(t,2)}`:""}
});

console.log(response.choices[0].message.content);
      `,{baseIndent:8})},{title:"curl",language:"shell",code:(0,w.getCURLExample)({data:k.default`{
            "model": "${e}",
            "messages": [
              {
                "role": "user",
                "content": [
                  {
                    "type": "image_url",
                    "image_url": {
                      "url": "${D}"
                    }
                  },
                  {
                    "type": "text",
                    "text": "${M}"
                  }
                ]
              }
            ]${t?`,
            "provider": ${(0,O.indentObjectParam)(t,16)}`:""}
        }`})}])(t);default:return(0,T.getChatCompletionExamples)(t)}},ea=e=>{let a,s,i,l,d,c,u=(0,n.c)(16),{examples:g,slug:h,inputModalities:f,provider:x,quickStartExampleType:y}=e,b=void 0===h?"openai/gpt-3.5-turbo":h;if(u[0]!==g||u[1]!==x||u[2]!==y||u[3]!==b||u[4]!==f){let e=void 0===f?[o.InputModality.Text]:f;a=g??en(y,{slug:b,inputModalities:e,provider:x}),u[0]=g,u[1]=x,u[2]=y,u[3]=b,u[4]=f,u[5]=a}else a=u[5];let _=a;return u[6]!==y?(s=(e=>{switch(e){case r.QuickStartExampleType.Embeddings:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)("p",{children:"OpenRouter provides an OpenAI-compatible embeddings API that you can call directly, or using the OpenAI SDK."}),(0,t.jsxs)("p",{children:["In the examples below, the"," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/requests#request-headers",className:"text-sm",children:"OpenRouter-specific headers"})," ","are optional. Setting them allows your app to appear on the OpenRouter leaderboards."]})]});case r.QuickStartExampleType.ImageInputEmbeddings:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)("p",{children:["OpenRouter supports image input embeddings for models that can generate embeddings from both text and images. Pass multimodal content using the ",(0,t.jsx)(m,{children:"content"})," ","array format with ",(0,t.jsx)(m,{children:"text"})," and ",(0,t.jsx)(m,{children:"image_url"})," ","components."," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/api_reference/embeddings#image-input",className:"text-sm",children:"Learn more about image embeddings"}),"."]}),(0,t.jsxs)("p",{children:["In the examples below, the"," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/requests#request-headers",className:"text-sm",children:"OpenRouter-specific headers"})," ","are optional. Setting them allows your app to appear on the OpenRouter leaderboards."]})]});case r.QuickStartExampleType.FastApply:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)("p",{children:"FastApply allows you to apply code edits by providing the original code, the desired changes, and instructions. The model will merge the changes intelligently."}),(0,t.jsxs)("p",{children:["In the examples below, the"," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/requests#request-headers",className:"text-sm",children:"OpenRouter-specific headers"})," ","are optional. Setting them allows your app to appear on the OpenRouter leaderboards."]})]});case r.QuickStartExampleType.Reasoning:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)("p",{children:["OpenRouter supports reasoning-enabled models that can show their step-by-step thinking process. Use the ",(0,t.jsx)(m,{children:"reasoning"})," parameter in your request to enable reasoning, and access the ",(0,t.jsx)(m,{children:"reasoning_details"})," array in the response to see the model's internal reasoning before the final answer. When continuing a conversation, preserve the complete ",(0,t.jsx)(m,{children:"reasoning_details"})," when passing messages back to the model so it can continue reasoning from where it left off."," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/use-cases/reasoning-tokens",className:"text-sm",children:"Learn more about reasoning tokens"}),"."]}),(0,t.jsxs)("p",{children:["In the examples below, the"," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/requests#request-headers",className:"text-sm",children:"OpenRouter-specific headers"})," ","are optional. Setting them allows your app to appear on the OpenRouter leaderboards."]})]});case r.QuickStartExampleType.ImageGeneration:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)("p",{children:["OpenRouter supports image generation models that can output both text and images. These models can create images from text prompts when you specify"," ",(0,t.jsx)(m,{children:'modalities: ["image", "text"]'})," in your request. The generated images are returned as base64-encoded data URLs in the assistant message."," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/features/multimodal/image-generation",className:"text-sm",children:"Learn more about image generation"}),"."]}),(0,t.jsxs)("p",{children:["In the examples below, the"," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/requests#request-headers",className:"text-sm",children:"OpenRouter-specific headers"})," ","are optional. Setting them allows your app to appear on the OpenRouter leaderboards."]})]});case r.QuickStartExampleType.ImageGenerationWithoutText:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)("p",{children:["OpenRouter supports image generation models that only output images and not text. These models can create images from text prompts when you specify"," ",(0,t.jsx)(m,{children:'modalities: ["image"]'})," in your request. The generated images are returned as base64-encoded data URLs in the assistant message."," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/features/multimodal/image-generation",className:"text-sm",children:"Learn more about image generation"}),"."]}),(0,t.jsxs)("p",{children:["In the examples below, the"," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/requests#request-headers",className:"text-sm",children:"OpenRouter-specific headers"})," ","are optional. Setting them allows your app to appear on the OpenRouter leaderboards."]})]});case r.QuickStartExampleType.VideoGeneration:return(0,t.jsxs)("p",{children:["OpenRouter supports video generation models that can create videos from text prompts or image inputs. Submit a generation request with your model, then poll the returned URL to check the status. Once complete, the response includes URLs to download the generated video."," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/features/multimodal/video-generation",className:"text-sm",children:"Learn more about video generation"}),"."]});case r.QuickStartExampleType.Rerank:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)("p",{children:"OpenRouter provides a rerank API that reorders documents by relevance to a query. Pass a query and a list of documents, and the model returns them ranked by relevance score."}),(0,t.jsxs)("p",{children:["In the examples below, the"," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/requests#request-headers",className:"text-sm",children:"OpenRouter-specific headers"})," ","are optional. Setting them allows your app to appear on the OpenRouter leaderboards."]})]});case r.QuickStartExampleType.TTS:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)("p",{children:"OpenRouter provides a text-to-speech API that converts text into natural-sounding audio. Send text and a voice selection, and receive raw audio bytes in your chosen format."}),(0,t.jsxs)("p",{children:["The response is a raw audio stream (not JSON). The generation ID is returned in the"," ",(0,t.jsx)(m,{children:"X-Generation-Id"})," response header for tracking."]})]});case r.QuickStartExampleType.STT:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)("p",{children:"OpenRouter provides a speech-to-text API that transcribes audio into text. Send base64-encoded audio with a model, and receive the transcribed text in JSON."}),(0,t.jsxs)("p",{children:["The generation ID is returned in the ",(0,t.jsx)(m,{children:"X-Generation-Id"})," response header for tracking."]})]});case r.QuickStartExampleType.OCR:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)("p",{children:["OpenRouter supports OCR models that can extract text, tables, formulas, and layout information from document images. Send an image via the standard chat completions API with an OCR-specific prompt, and the model returns structured output such as Markdown, LaTeX, or HTML. See the"," ",(0,t.jsx)(p.ExternalLink,{href:"https://github.com/baidubce/qianfan-models-cookbook/tree/main/qianfan-ocr",className:"text-sm",children:"Qianfan OCR cookbook"})," ","for detailed usage examples including document parsing, layout analysis, element recognition, and key information extraction."]}),(0,t.jsxs)("p",{children:["In the examples below, the"," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/requests#request-headers",className:"text-sm",children:"OpenRouter-specific headers"})," ","are optional. Setting them allows your app to appear on the OpenRouter leaderboards."]})]});case r.QuickStartExampleType.AudioOutput:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)("p",{children:["OpenRouter supports audio output from models with speech capabilities. Set"," ",(0,t.jsx)(m,{children:'modalities: ["text", "audio"]'})," and provide an"," ",(0,t.jsx)(m,{children:"audio"})," configuration with your desired voice and format. Audio output requires streaming — the response is delivered as SSE chunks containing base64-encoded audio data and a transcript."," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/features/multimodal/audio",className:"text-sm",children:"Learn more about audio"}),"."]}),(0,t.jsxs)("p",{children:["In the examples below, the"," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/requests#request-headers",className:"text-sm",children:"OpenRouter-specific headers"})," ","are optional. Setting them allows your app to appear on the OpenRouter leaderboards."]})]});default:return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsxs)("p",{children:["OpenRouter provides an OpenAI-compatible completion API to ",E.MarketingMetrics.ModelCount," ","models & providers that you can call directly, or using the OpenAI SDK. Additionally, some third-party SDKs are available."]}),(0,t.jsxs)("p",{children:["In the examples below, the"," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/requests#request-headers",className:"text-sm",children:"OpenRouter-specific headers"})," ","are optional. Setting them allows your app to appear on the OpenRouter leaderboards."]})]})}})(y),u[6]=y,u[7]=s):s=u[7],u[8]!==_||u[9]!==b?(i=(0,t.jsx)(I,{className:"mb-6",examples:_,slug:b}),u[8]=_,u[9]=b,u[10]=i):i=u[10],u[11]===Symbol.for("react.memo_cache_sentinel")?(l=(0,t.jsx)("h2",{children:"Using third-party SDKs"}),u[11]=l):l=u[11],u[12]===Symbol.for("react.memo_cache_sentinel")?(d=(0,t.jsxs)("p",{children:["For information about using third-party SDKs and frameworks with OpenRouter, please see our"," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/guides/community/frameworks-and-integrations-overview",className:"text-sm",children:"frameworks documentation"}),"."]}),u[12]=d):d=u[12],u[13]!==s||u[14]!==i?(c=(0,t.jsxs)("div",{className:"space-y-3 text-sm text-muted-foreground [&_h2]:text-sm [&_h2]:font-medium [&_h2]:tracking-normal [&_h2]:text-foreground",children:[s,i,l,d]}),u[13]=s,u[14]=i,u[15]=c):c=u[15],c};var es=e.i(162715),eo=e.i(564940),er=e.i(874911),ei=e.i(748700);function el(e){let a,s,o,r,i,l,d,c,p,m,g,h,f=(0,n.c)(26),{supportedParameters:x}=e;if(f[0]!==x){let e=Object.entries(x);d="space-y-3",f[9]===Symbol.for("react.memo_cache_sentinel")?(c=(0,t.jsx)("h3",{className:"text-sm font-medium tracking-normal text-foreground",children:"Supported Parameters"}),f[9]=c):c=f[9],o=er.Card,s=u.Table,i="text-sm",f[10]===Symbol.for("react.memo_cache_sentinel")?(l=(0,t.jsx)(u.TableHeader,{children:(0,t.jsxs)(u.TableRow,{children:[(0,t.jsx)(u.TableHead,{children:"Parameter"}),(0,t.jsx)(u.TableHead,{children:"Type"}),(0,t.jsx)(u.TableHead,{children:"Values"})]})}),f[10]=l):l=f[10],a=u.TableBody,r=e.map(ed),f[0]=x,f[1]=a,f[2]=s,f[3]=o,f[4]=r,f[5]=i,f[6]=l,f[7]=d,f[8]=c}else a=f[1],s=f[2],o=f[3],r=f[4],i=f[5],l=f[6],d=f[7],c=f[8];return f[11]!==a||f[12]!==r?(p=(0,t.jsx)(a,{children:r}),f[11]=a,f[12]=r,f[13]=p):p=f[13],f[14]!==s||f[15]!==i||f[16]!==l||f[17]!==p?(m=(0,t.jsxs)(s,{className:i,children:[l,p]}),f[14]=s,f[15]=i,f[16]=l,f[17]=p,f[18]=m):m=f[18],f[19]!==o||f[20]!==m?(g=(0,t.jsx)(o,{children:m}),f[19]=o,f[20]=m,f[21]=g):g=f[21],f[22]!==d||f[23]!==c||f[24]!==g?(h=(0,t.jsxs)("div",{className:d,children:[c,g]}),f[22]=d,f[23]=c,f[24]=g,f[25]=h):h=f[25],h}function ed(e){let[n,a]=e;return(0,t.jsxs)(u.TableRow,{children:[(0,t.jsx)(u.TableCell,{children:(0,t.jsx)("code",{className:"bg-transparent font-mono text-foreground",children:n})}),(0,t.jsx)(u.TableCell,{children:function(e){switch(e.type){case ei.CapabilityType.Enum:return"enum";case ei.CapabilityType.Range:return"range";case ei.CapabilityType.Boolean:return"boolean";default:return"unknown"}}(a)}),(0,t.jsx)(u.TableCell,{children:function(e){switch(e.type){case ei.CapabilityType.Enum:return e.values.join(", ");case ei.CapabilityType.Range:return`${e.min}–${e.max}`;case ei.CapabilityType.Boolean:return"Supported";default:return"—"}}(a)})]},n)}var ec=e.i(133974);function ep(e){let a,s,o,r,i,l=(0,n.c)(7),{passthroughByProvider:d}=e;return l[0]===Symbol.for("react.memo_cache_sentinel")?(a=(0,t.jsx)("h3",{className:"text-sm font-medium tracking-normal text-foreground",children:"Provider Passthrough Parameters"}),l[0]=a):a=l[0],l[1]===Symbol.for("react.memo_cache_sentinel")?(s=(0,t.jsxs)("p",{className:"text-xs text-muted-foreground",children:["Provider-specific keys accepted under"," ",(0,t.jsx)("code",{className:"bg-transparent font-mono text-xs",children:"provider.options"}),"."]}),l[1]=s):s=l[1],l[2]===Symbol.for("react.memo_cache_sentinel")?(o=(0,t.jsx)(ec.TableHeader,{children:(0,t.jsxs)(ec.TableRow,{children:[(0,t.jsx)(ec.TableHead,{className:"text-xs",children:"Provider"}),(0,t.jsx)(ec.TableHead,{className:"text-xs",children:"Parameters"})]})}),l[2]=o):o=l[2],l[3]!==d?(r=d.map(em),l[3]=d,l[4]=r):r=l[4],l[5]!==r?(i=(0,t.jsxs)("div",{className:"space-y-3",children:[a,s,(0,t.jsx)("div",{className:"overflow-x-auto rounded-lg border",children:(0,t.jsxs)(ec.Table,{children:[o,(0,t.jsx)(ec.TableBody,{children:r})]})})]}),l[5]=r,l[6]=i):i=l[6],i}function em(e){return(0,t.jsxs)(ec.TableRow,{children:[(0,t.jsx)(ec.TableCell,{className:"py-2",children:(0,t.jsx)("span",{className:"text-xs text-muted-foreground",children:e.providerName})}),(0,t.jsx)(ec.TableCell,{className:"py-2",children:(0,t.jsx)("div",{className:"flex flex-wrap gap-1.5",children:e.parameters.map(eu)})})]},e.providerName)}function eu(e){return(0,t.jsx)("code",{className:"rounded bg-muted px-1.5 py-0.5 font-mono text-xs font-medium",children:e},e)}var eg=e.i(449242),eh=e.i(852413),ef=e.i(543508),ex=e.i(917138);let ey=[{label:"Authorization",value:"Bearer $OPENROUTER_API_KEY",isRequired:!0},{label:"Content-Type",value:"application/json",isRequired:!0},{label:"HTTP-Referer",value:"optional — your site URL, for rankings",isRequired:!1},{label:"X-Title",value:"optional — your site name, for rankings",isRequired:!1}],eb=new Map([[ef.CHAT_COMPLETIONS_ENDPOINT,"Sends a request for a model response for the given chat conversation. Supports both streaming and non-streaming modes."],[ef.RESPONSES_ENDPOINT,"Creates a streaming or non-streaming response using the OpenAI Responses API format."],[ef.MESSAGES_ENDPOINT,"Creates a message using the Anthropic Messages API format. Supports text, images, PDFs, tools, and extended thinking."],["https://openrouter.ai/api/v1/embeddings","Submits an embedding request to the embeddings router"],["https://openrouter.ai/api/v1/rerank","Submits a rerank request to the rerank router"],["https://openrouter.ai/api/v1/audio/speech","Synthesizes audio from the input text. Returns a raw audio bytestream in the requested format (e.g. mp3, pcm, wav)."],["https://openrouter.ai/api/v1/audio/transcriptions","Transcribes audio into text. Accepts base64-encoded audio input and returns the transcribed text."],["https://openrouter.ai/api/v1/videos","Submits a video generation request and returns a polling URL to check status"],[ef.IMAGE_API_ENDPOINT,"Submits an image generation request. Returns base64-encoded images or streams partial results via SSE."]]);function e_(){let e,a,o=(0,n.c)(11),i=(0,g.usePosthogClient)(),{model:l}=(0,b.useModelPage)();o[0]!==l?(e=(0,s.getModelVariantSlug)(l),o[0]=l,o[1]=e):e=o[1];let d=e;if((0,eg.isImageOnlyModel)({quickStartExampleType:l.quick_start_example_type,outputModalities:l.output_modalities})){let e;return o[2]!==d?(e=(0,t.jsx)(ej,{modelSlug:d}),o[2]=d,o[3]=e):e=o[3],e}if(l.quick_start_example_type===r.QuickStartExampleType.ImageGeneration){let e;return o[4]!==l||o[5]!==d||o[6]!==i?(e=(0,t.jsx)(e$,{model:l,modelSlug:d,posthog:i}),o[4]=l,o[5]=d,o[6]=i,o[7]=e):e=o[7],e}return o[8]!==l||o[9]!==d?(a=(0,t.jsx)(eP,{model:l,modelSlug:d}),o[8]=l,o[9]=d,o[10]=a):a=o[10],a}function ej(e){let a,s,r,i,l,d,c,u,g,h,f,x,y=(0,n.c)(25),{modelSlug:b}=e,{data:_}=(0,ex.useImageDiscovery)(b);y[0]===Symbol.for("react.memo_cache_sentinel")?(a=(0,ef.getEndpointReferencesForOutputModalities)([o.OutputModality.Image],{useImageApi:!0}),y[0]=a):a=y[0];let j=a;y[1]!==b?(s=(0,eh.getDedicatedImageApiExamples)({slug:b}),y[1]=b,y[2]=s):s=y[2];let $=s;return y[3]===Symbol.for("react.memo_cache_sentinel")?(r=(0,t.jsx)(es.ApiKeyStep,{}),y[3]=r):r=y[3],y[4]===Symbol.for("react.memo_cache_sentinel")?(i=(0,t.jsxs)("div",{className:"flex items-center gap-2.5",children:[(0,t.jsx)(eo.StepNumber,{n:2}),(0,t.jsx)("h3",{className:"text-sm font-medium tracking-normal text-foreground",children:"Generate an image"})]}),y[4]=i):i=y[4],y[5]!==b?(l=(0,t.jsxs)("p",{className:"ml-[30px] text-sm text-muted-foreground",children:["Use the dedicated Image API with ",(0,t.jsx)(m,{children:b}),":"]}),y[5]=b,y[6]=l):l=y[6],y[7]===Symbol.for("react.memo_cache_sentinel")?(d=(0,t.jsxs)("p",{className:"mb-3 text-sm text-muted-foreground",children:["Send a prompt and receive generated images as base64-encoded data."," ",(0,t.jsx)(p.ExternalLink,{href:"/docs/features/multimodal/image-generation",className:"text-sm",children:"Learn more about image generation"}),"."]}),y[7]=d):d=y[7],y[8]!==$||y[9]!==b?(c=(0,t.jsxs)("div",{className:"ml-[30px]",children:[d,(0,t.jsx)(I,{examples:$,slug:b})]}),y[8]=$,y[9]=b,y[10]=c):c=y[10],y[11]!==l||y[12]!==c?(u=(0,t.jsxs)("div",{className:"space-y-3",children:[i,l,c]}),y[11]=l,y[12]=c,y[13]=u):u=y[13],y[14]!==b?(g=j.length>0&&(0,t.jsx)(eI,{references:j,modelSlug:b}),y[14]=b,y[15]=g):g=y[15],y[16]!==_?(h=_?.supportedParameters&&Object.keys(_.supportedParameters).length>0&&(0,t.jsx)(el,{supportedParameters:_.supportedParameters}),y[16]=_,y[17]=h):h=y[17],y[18]!==_?(f=_?.passthroughByProvider&&_.passthroughByProvider.length>0&&(0,t.jsx)(ep,{passthroughByProvider:_.passthroughByProvider}),y[18]=_,y[19]=f):f=y[19],y[20]!==h||y[21]!==f||y[22]!==u||y[23]!==g?(x=(0,t.jsx)("div",{className:"flex w-full flex-col gap-4",children:(0,t.jsxs)("div",{className:"space-y-8",children:[r,u,g,h,f]})}),y[20]=h,y[21]=f,y[22]=u,y[23]=g,y[24]=x):x=y[24],x}function e$(e){let a,s,r,i,d,p,m,u,g,h,f,y,b=(0,n.c)(31),{model:_,modelSlug:j,posthog:$}=e;b[0]===Symbol.for("react.memo_cache_sentinel")?(a={output_modalities:(0,x.parseAsArrayOf)((0,x.parseAsStringEnum)(Object.values(o.OutputModality)))},b[0]=a):a=b[0];let[P,v]=(0,x.useQueryStates)(a),{output_modalities:I}=P;b[1]!==I?(s=(0,eg.getApiTabForOutputModalities)(I),b[1]=I,b[2]=s):s=b[2];let E=s;b[3]!==j||b[4]!==$||b[5]!==v?(r=function(e){v({output_modalities:(0,eg.getOutputModalitiesForApiTab)(e)}),$.capture(l.PostHogEvent.ClickApiModalityTab,{model:j,tab:e})},b[3]=j,b[4]=$,b[5]=v,b[6]=r):r=b[6];let A=r;b[7]!==A?(i=()=>A(eg.API_TAB.ChatCompletions),b[7]=A,b[8]=i):i=b[8];let O=E===eg.API_TAB.ChatCompletions?"bg-secondary text-accent-foreground":"text-muted-foreground hover:bg-card-hover hover:text-accent-foreground";b[9]!==O?(d=(0,c.cn)("rounded-md px-3 py-1.5 text-sm font-medium transition-colors",O),b[9]=O,b[10]=d):d=b[10],b[11]!==i||b[12]!==d?(p=(0,t.jsx)("button",{type:"button",onClick:i,className:d,children:"Chat Completions"}),b[11]=i,b[12]=d,b[13]=p):p=b[13],b[14]!==A?(m=()=>A(eg.API_TAB.ImageApi),b[14]=A,b[15]=m):m=b[15];let k=E===eg.API_TAB.ImageApi?"bg-secondary text-accent-foreground":"text-muted-foreground hover:bg-card-hover hover:text-accent-foreground";return b[16]!==k?(u=(0,c.cn)("rounded-md px-3 py-1.5 text-sm font-medium transition-colors",k),b[16]=k,b[17]=u):u=b[17],b[18]!==u||b[19]!==m?(g=(0,t.jsx)("button",{type:"button",onClick:m,className:u,children:"Image API"}),b[18]=u,b[19]=m,b[20]=g):g=b[20],b[21]!==g||b[22]!==p?(h=(0,t.jsxs)("div",{className:"flex items-center gap-1",children:[p,g]}),b[21]=g,b[22]=p,b[23]=h):h=b[23],b[24]!==E||b[25]!==_||b[26]!==j?(f=E===eg.API_TAB.ChatCompletions?(0,t.jsx)(eP,{model:_,modelSlug:j}):(0,t.jsx)(ej,{modelSlug:j}),b[24]=E,b[25]=_,b[26]=j,b[27]=f):f=b[27],b[28]!==h||b[29]!==f?(y=(0,t.jsxs)("div",{className:"flex w-full flex-col gap-4",children:[h,f]}),b[28]=h,b[29]=f,b[30]=y):y=b[30],y}function eP(e){let a,s,o,r,i,l,c,p,u,g,y,b,_,$,P,v=(0,n.c)(41),{model:I,modelSlug:E}=e;v[0]!==I.output_modalities?(a=(0,ef.getEndpointReferencesForOutputModalities)(I.output_modalities),v[0]=I.output_modalities,v[1]=a):a=v[1];let A=a,O=A[0]?.endpoint===ef.CHAT_COMPLETIONS_ENDPOINT;v[2]===Symbol.for("react.memo_cache_sentinel")?(s={quantization:(0,x.parseAsStringEnum)(Object.values(d.Quantization))},v[2]=s):s=v[2];let[k]=(0,x.useQueryStates)(s),{quantization:w}=k;v[3]!==w?(o=function({quantization:e}){return e?{quantizations:[e]}:null}({quantization:w})??void 0,v[3]=w,v[4]=o):o=v[4];let R=o;v[5]!==I.input_modalities||v[6]!==I.quick_start_example_type||v[7]!==E||v[8]!==R?(r=en(I.quick_start_example_type,{slug:E,inputModalities:I.input_modalities,provider:R}),v[5]=I.input_modalities,v[6]=I.quick_start_example_type,v[7]=E,v[8]=R,v[9]=r):r=v[9];let T=r;v[10]!==I.default_parameters||v[11]!==I.endpoint?.supported_parameters?(i=()=>{let e=I.endpoint?.supported_parameters;if(!e||0===e.length)return[];let t=I.default_parameters;return e.filter(ev).map(e=>(function(e,t){var n;let a=h.parametersMap[e];if(!a)return{name:e,typeLabel:"unknown",defaultValue:null,description:"Supported by this endpoint."};let s=function(e,t){return t&&eR.has(e)?t[e]??null:null}(e,t);return{name:a.name,typeLabel:(n=a)instanceof f.NumberPD||n instanceof f.NumberRangePD?n.metadata.type:n instanceof f.BooleanPD?"boolean":n instanceof f.EnumPD?"enum":n instanceof f.MapPD||n instanceof f.ArrayPD?n.type:n instanceof f.StringOrObjectPD?"string or object":"unknown",defaultValue:function(e,t){if(e instanceof f.NumberRangePD||e instanceof f.NumberPD){let n=t??e.metadata.defaultValue;return null===n?null:"integer"===e.metadata.type?n.toFixed(0):String(n)}return e instanceof f.BooleanPD||e instanceof f.EnumPD?null===e.metadata.defaultValue?null:String(e.metadata.defaultValue):e instanceof f.MapPD||e instanceof f.ArrayPD||e instanceof f.StringOrObjectPD?null===e.metadata.defaultValue?null:JSON.stringify(e.metadata.defaultValue):null}(a,s),description:function(e){let t=e.split(/\.\s/)[0];if(!t)return e;let n=t.replaceAll(/\s+/g," ").trim();return n.endsWith(".")?n:`${n}.`}(a.description)}})(e,t))},v[10]=I.default_parameters,v[11]=I.endpoint?.supported_parameters,v[12]=i):i=v[12],I.endpoint?.supported_parameters,v[13]!==i?(l=i(),v[13]=i,v[14]=l):l=v[14];let S=l;if(v[15]===Symbol.for("react.memo_cache_sentinel")?(c=(0,t.jsx)(es.ApiKeyStep,{}),v[15]=c):c=v[15],v[16]===Symbol.for("react.memo_cache_sentinel")?(p=(0,t.jsxs)("div",{className:"flex items-center gap-2.5",children:[(0,t.jsx)(eo.StepNumber,{n:2}),(0,t.jsx)("h3",{className:"text-sm font-medium tracking-normal text-foreground",children:"Make your first request"})]}),v[16]=p):p=v[16],v[17]!==E?(u=(0,t.jsxs)("p",{className:"ml-[30px] text-sm text-muted-foreground",children:["Use ",(0,t.jsx)(m,{children:E})," with the OpenRouter API:"]}),v[17]=E,v[18]=u):u=v[18],v[19]!==T||v[20]!==I.input_modalities||v[21]!==I.quick_start_example_type||v[22]!==E||v[23]!==R?(g=(0,t.jsx)("div",{className:"ml-[30px]",children:(0,t.jsx)(ea,{examples:T,slug:E,inputModalities:I.input_modalities,quickStartExampleType:I.quick_start_example_type,provider:R})}),v[19]=T,v[20]=I.input_modalities,v[21]=I.quick_start_example_type,v[22]=E,v[23]=R,v[24]=g):g=v[24],v[25]!==u||v[26]!==g?(y=(0,t.jsxs)("div",{className:"space-y-3",children:[p,u,g]}),v[25]=u,v[26]=g,v[27]=y):y=v[27],v[28]!==E||v[29]!==O)b=O&&(0,t.jsxs)("div",{className:"space-y-3",children:[(0,t.jsxs)("div",{className:"flex items-center gap-2.5",children:[(0,t.jsx)(eo.StepNumber,{n:3}),(0,t.jsx)("h3",{className:"text-sm font-medium tracking-normal text-foreground",children:"Enable streaming"})]}),(0,t.jsxs)("p",{className:"ml-[30px] text-sm text-muted-foreground",children:["Add ",(0,t.jsx)(m,{children:'"stream": true'})," to your request body to receive responses as server-sent events:"]}),(0,t.jsx)("div",{className:"ml-[30px]",children:(0,t.jsx)(j.ApiCodeBlock,{language:"shell",value:`
    curl -N https://openrouter.ai/api/v1/chat/completions \\
      -H "Content-Type: application/json" \\
      -H "Authorization: Bearer $OPENROUTER_API_KEY" \\
      -d '{
      "model": "${E}",
      "stream": true,
      "messages": [
        {"role": "user", "content": "Hello"}
      ]
    }'
  `})})]}),v[28]=E,v[29]=O,v[30]=b;else b=v[30];return v[31]!==A||v[32]!==E?(_=A.length>0&&(0,t.jsx)(eI,{references:A,modelSlug:E}),v[31]=A,v[32]=E,v[33]=_):_=v[33],v[34]!==S?($=S.length>0&&(0,t.jsx)(ek,{params:S}),v[34]=S,v[35]=$):$=v[35],v[36]!==y||v[37]!==b||v[38]!==_||v[39]!==$?(P=(0,t.jsx)("div",{className:"flex w-full flex-col gap-4",children:(0,t.jsxs)("div",{className:"space-y-8",children:[c,y,b,_,$]})}),v[36]=y,v[37]=b,v[38]=_,v[39]=$,v[40]=P):P=v[40],P}function ev(e){return!i.INTERNAL_PARAMETERS.has(e)}function eI(e){let a,s,o,r=(0,n.c)(8),{references:i,modelSlug:l}=e;if(r[0]===Symbol.for("react.memo_cache_sentinel")?(a=(0,t.jsx)("h3",{className:"text-foreground",children:"Endpoint"}),r[0]=a):a=r[0],r[1]!==l||r[2]!==i){let e;r[4]!==l?(e=e=>{var n;return(0,t.jsx)(eE,{description:(n=e.endpoint,eb.get(n)??"OpenRouter normalizes requests and responses across providers for this endpoint."),endpoint:e.endpoint,modelSlug:l,docsHref:e.docsHref},e.endpoint)},r[4]=l,r[5]=e):e=r[5],s=i.map(e),r[1]=l,r[2]=i,r[3]=s}else s=r[3];return r[6]!==s?(o=(0,t.jsxs)("section",{className:"space-y-4",children:[a,(0,t.jsx)("div",{className:"space-y-3",children:s})]}),r[6]=s,r[7]=o):o=r[7],o}function eE(e){let s,o,r,i,l,d,c,m,u,g=(0,n.c)(19),{endpoint:h,modelSlug:f,description:x,docsHref:y}=e;return g[0]!==x?(s=(0,t.jsx)("p",{className:"text-sm text-muted-foreground",children:x}),g[0]=x,g[1]=s):s=g[1],g[2]!==y?(o=y?(0,t.jsxs)(p.ExternalLink,{href:y,children:["Docs",(0,t.jsx)(a.ArrowTopRightOnSquareIcon,{className:"ml-0.5 inline size-3"})]}):null,g[2]=y,g[3]=o):o=g[3],g[4]!==s||g[5]!==o?(r=(0,t.jsxs)("div",{className:"flex flex-wrap items-center gap-x-2 gap-y-1",children:[s,o]}),g[4]=s,g[5]=o,g[6]=r):r=g[6],g[7]===Symbol.for("react.memo_cache_sentinel")?(i=(0,t.jsx)("span",{className:"font-mono text-xs font-medium text-positive-text",children:"POST"}),g[7]=i):i=g[7],g[8]!==h?(l=(0,t.jsxs)("div",{className:"flex items-center gap-2 border-b bg-muted px-4 py-3",children:[i,(0,t.jsx)("code",{className:"break-all bg-transparent font-mono text-xs text-muted-foreground",children:h})]}),g[8]=h,g[9]=l):l=g[9],g[10]===Symbol.for("react.memo_cache_sentinel")?(d=ey.map(eA),g[10]=d):d=g[10],g[11]!==f?(c=(0,t.jsxs)("div",{className:"space-y-2 px-4 py-3",children:[d,(0,t.jsx)(eO,{label:"Model",value:f,isRequired:!0})]}),g[11]=f,g[12]=c):c=g[12],g[13]!==l||g[14]!==c?(m=(0,t.jsxs)("div",{className:"overflow-hidden rounded-lg border",children:[l,c]}),g[13]=l,g[14]=c,g[15]=m):m=g[15],g[16]!==r||g[17]!==m?(u=(0,t.jsxs)("div",{className:"space-y-3",children:[r,m]}),g[16]=r,g[17]=m,g[18]=u):u=g[18],u}function eA(e){return(0,t.jsx)(eO,{label:e.label,value:e.value,isRequired:e.isRequired},e.label)}function eO(e){let a,s,o,r,i=(0,n.c)(10),{label:l,value:d,isRequired:p}=e;i[0]!==l?(a=(0,t.jsx)("span",{className:"shrink-0 text-muted-foreground sm:w-28",children:l}),i[0]=l,i[1]=a):a=i[1];let m=void 0!==p&&p?"text-foreground":"text-muted-foreground";return i[2]!==m?(s=(0,c.cn)("bg-transparent font-mono text-xs",m),i[2]=m,i[3]=s):s=i[3],i[4]!==s||i[5]!==d?(o=(0,t.jsx)("code",{className:s,children:d}),i[4]=s,i[5]=d,i[6]=o):o=i[6],i[7]!==a||i[8]!==o?(r=(0,t.jsxs)("div",{className:"flex flex-col gap-1 text-xs sm:flex-row sm:items-start sm:gap-3",children:[a,o]}),i[7]=a,i[8]=o,i[9]=r):r=i[9],r}function ek(e){let a,s,o,r,i=(0,n.c)(6),{params:l}=e;return i[0]===Symbol.for("react.memo_cache_sentinel")?(a=(0,t.jsx)("h3",{className:"text-sm font-medium tracking-normal text-foreground",children:"Parameters"}),i[0]=a):a=i[0],i[1]===Symbol.for("react.memo_cache_sentinel")?(s=(0,t.jsx)(u.TableHeader,{children:(0,t.jsxs)(u.TableRow,{children:[(0,t.jsx)(u.TableHead,{children:"Name"}),(0,t.jsx)(u.TableHead,{children:"Type"}),(0,t.jsx)(u.TableHead,{children:"Default"}),(0,t.jsx)(u.TableHead,{children:"Description"})]})}),i[1]=s):s=i[1],i[2]!==l?(o=l.map(ew),i[2]=l,i[3]=o):o=i[3],i[4]!==o?(r=(0,t.jsxs)("div",{className:"space-y-3",children:[a,(0,t.jsxs)(u.Table,{children:[s,(0,t.jsx)(u.TableBody,{children:o})]})]}),i[4]=o,i[5]=r):r=i[5],r}function ew(e){return(0,t.jsxs)(u.TableRow,{children:[(0,t.jsx)(u.TableCell,{children:(0,t.jsx)("code",{className:"bg-transparent font-mono text-foreground",children:e.name})}),(0,t.jsx)(u.TableCell,{children:e.typeLabel}),(0,t.jsx)(u.TableCell,{children:null!==e.defaultValue?(0,t.jsx)("code",{className:"bg-transparent font-mono text-foreground",children:e.defaultValue}):(0,t.jsx)("span",{className:"text-muted-foreground",children:"—"})}),(0,t.jsx)(u.TableCell,{children:e.description})]},e.name)}let eR=new Set(["temperature","top_p","top_k","frequency_penalty","presence_penalty","repetition_penalty"]);e.s(["ModelAPI",0,function(){let e,a=(0,n.c)(1);return a[0]===Symbol.for("react.memo_cache_sentinel")?(e=(0,t.jsx)(y.Suspense,{fallback:null,children:(0,t.jsx)(e_,{})}),a[0]=e):e=a[0],e}],495916)}]);

//# sourceMappingURL=1plrlwe8f7z8m.js.map
//# chunkId=019f9c7a-1007-74f3-9ad3-679a845667ea