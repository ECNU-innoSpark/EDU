!function(){try{var e="undefined"!=typeof window?window:"undefined"!=typeof global?global:"undefined"!=typeof globalThis?globalThis:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&(e._posthogChunkIds=e._posthogChunkIds||{},e._posthogChunkIds[n]="019f9c7a-132c-7d20-b6d9-c3dcc3e8588e")}catch(e){}}();(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,833481,e=>{"use strict";var t,n=Symbol.for("immer-nothing"),r=Symbol.for("immer-draftable"),i=Symbol.for("immer-state");function a(e){throw Error(`[Immer] minified error nr: ${e}. Full error at: https://bit.ly/3cXEKWf`)}var o=Object.getPrototypeOf;function s(e){return!!e&&!!e[i]}function l(e){return!!e&&(c(e)||Array.isArray(e)||!!e[r]||!!e.constructor?.[r]||g(e)||h(e))}var u=Object.prototype.constructor.toString();function c(e){if(!e||"object"!=typeof e)return!1;let t=o(e);if(null===t)return!0;let n=Object.hasOwnProperty.call(t,"constructor")&&t.constructor;return n===Object||"function"==typeof n&&Function.toString.call(n)===u}function d(e,t){0===p(e)?Reflect.ownKeys(e).forEach(n=>{t(n,e[n],e)}):e.forEach((n,r)=>t(r,n,e))}function p(e){let t=e[i];return t?t.type_:Array.isArray(e)?1:g(e)?2:3*!!h(e)}function m(e,t){return 2===p(e)?e.has(t):Object.prototype.hasOwnProperty.call(e,t)}function f(e,t,n){let r=p(e);2===r?e.set(t,n):3===r?e.add(n):e[t]=n}function g(e){return e instanceof Map}function h(e){return e instanceof Set}function _(e){return e.copy_||e.base_}function b(e,t){if(g(e))return new Map(e);if(h(e))return new Set(e);if(Array.isArray(e))return Array.prototype.slice.call(e);let n=c(e);if(!0!==t&&("class_only"!==t||n)){let t=o(e);return null!==t&&n?{...e}:Object.assign(Object.create(t),e)}{let t=Object.getOwnPropertyDescriptors(e);delete t[i];let n=Reflect.ownKeys(t);for(let r=0;r<n.length;r++){let i=n[r],a=t[i];!1===a.writable&&(a.writable=!0,a.configurable=!0),(a.get||a.set)&&(t[i]={configurable:!0,writable:!0,enumerable:a.enumerable,value:e[i]})}return Object.create(o(e),t)}}function y(e,t=!1){return w(e)||s(e)||!l(e)||(p(e)>1&&Object.defineProperties(e,{set:{value:v},add:{value:v},clear:{value:v},delete:{value:v}}),Object.freeze(e),t&&Object.values(e).forEach(e=>y(e,!0))),e}function v(){a(2)}function w(e){return Object.isFrozen(e)}var E={};function z(e){let t=E[e];return t||a(0,e),t}function x(e,t){t&&(z("Patches"),e.patches_=[],e.inversePatches_=[],e.patchListener_=t)}function P(e){j(e),e.drafts_.forEach(O),e.drafts_=null}function j(e){e===t&&(t=e.parent_)}function I(e){return t={drafts_:[],parent_:t,immer_:e,canAutoFreeze_:!0,unfinalizedDrafts_:0}}function O(e){let t=e[i];0===t.type_||1===t.type_?t.revoke_():t.revoked_=!0}function R(e,t){t.unfinalizedDrafts_=t.drafts_.length;let r=t.drafts_[0];return void 0!==e&&e!==r?(r[i].modified_&&(P(t),a(4)),l(e)&&(e=k(t,e),t.parent_||A(t,e)),t.patches_&&z("Patches").generateReplacementPatches_(r[i].base_,e,t.patches_,t.inversePatches_)):e=k(t,r,[]),P(t),t.patches_&&t.patchListener_(t.patches_,t.inversePatches_),e!==n?e:void 0}function k(e,t,n){if(w(t))return t;let r=t[i];if(!r)return d(t,(i,a)=>$(e,r,t,i,a,n)),t;if(r.scope_!==e)return t;if(!r.modified_)return A(e,r.base_,!0),r.base_;if(!r.finalized_){r.finalized_=!0,r.scope_.unfinalizedDrafts_--;let t=r.copy_,i=t,a=!1;3===r.type_&&(i=new Set(t),t.clear(),a=!0),d(i,(i,o)=>$(e,r,t,i,o,n,a)),A(e,t,!1),n&&e.patches_&&z("Patches").generatePatches_(r,n,e.patches_,e.inversePatches_)}return r.copy_}function $(e,t,n,r,i,a,o){if(s(i)){let o=k(e,i,a&&t&&3!==t.type_&&!m(t.assigned_,r)?a.concat(r):void 0);if(f(n,r,o),!s(o))return;e.canAutoFreeze_=!1}else o&&n.add(i);if(l(i)&&!w(i)){if(!e.immer_.autoFreeze_&&e.unfinalizedDrafts_<1)return;k(e,i),(!t||!t.scope_.parent_)&&"symbol"!=typeof r&&(g(n)?n.has(r):Object.prototype.propertyIsEnumerable.call(n,r))&&A(e,i)}}function A(e,t,n=!1){!e.parent_&&e.immer_.autoFreeze_&&e.canAutoFreeze_&&y(t,n)}var S={get(e,t){if(t===i)return e;let n=_(e);if(!m(n,t)){var r;let i;return r=e,(i=M(n,t))?"value"in i?i.value:i.get?.call(r.draft_):void 0}let a=n[t];return e.finalized_||!l(a)?a:a===T(e.base_,t)?(L(e),e.copy_[t]=B(a,e)):a},has:(e,t)=>t in _(e),ownKeys:e=>Reflect.ownKeys(_(e)),set(e,t,n){let r=M(_(e),t);if(r?.set)return r.set.call(e.draft_,n),!0;if(!e.modified_){let r=T(_(e),t),a=r?.[i];if(a&&a.base_===n)return e.copy_[t]=n,e.assigned_[t]=!1,!0;if((n===r?0!==n||1/n==1/r:n!=n&&r!=r)&&(void 0!==n||m(e.base_,t)))return!0;L(e),F(e)}return!!(e.copy_[t]===n&&(void 0!==n||t in e.copy_)||Number.isNaN(n)&&Number.isNaN(e.copy_[t]))||(e.copy_[t]=n,e.assigned_[t]=!0,!0)},deleteProperty:(e,t)=>(void 0!==T(e.base_,t)||t in e.base_?(e.assigned_[t]=!1,L(e),F(e)):delete e.assigned_[t],e.copy_&&delete e.copy_[t],!0),getOwnPropertyDescriptor(e,t){let n=_(e),r=Reflect.getOwnPropertyDescriptor(n,t);return r?{writable:!0,configurable:1!==e.type_||"length"!==t,enumerable:r.enumerable,value:n[t]}:r},defineProperty(){a(11)},getPrototypeOf:e=>o(e.base_),setPrototypeOf(){a(12)}},C={};function T(e,t){let n=e[i];return(n?_(n):e)[t]}function M(e,t){if(!(t in e))return;let n=o(e);for(;n;){let e=Object.getOwnPropertyDescriptor(n,t);if(e)return e;n=o(n)}}function F(e){!e.modified_&&(e.modified_=!0,e.parent_&&F(e.parent_))}function L(e){e.copy_||(e.copy_=b(e.base_,e.scope_.immer_.useStrictShallowCopy_))}function B(e,n){let r=g(e)?z("MapSet").proxyMap_(e,n):h(e)?z("MapSet").proxySet_(e,n):function(e,n){let r=Array.isArray(e),i={type_:+!!r,scope_:n?n.scope_:t,modified_:!1,finalized_:!1,assigned_:{},parent_:n,base_:e,draft_:null,copy_:null,revoke_:null,isManual_:!1},a=i,o=S;r&&(a=[i],o=C);let{revoke:s,proxy:l}=Proxy.revocable(a,o);return i.draft_=l,i.revoke_=s,l}(e,n);return(n?n.scope_:t).drafts_.push(r),r}function D(e){return s(e)||a(10,e),function e(t){let n;if(!l(t)||w(t))return t;let r=t[i];if(r){if(!r.modified_)return r.base_;r.finalized_=!0,n=b(t,r.scope_.immer_.useStrictShallowCopy_)}else n=b(t,!0);return d(n,(t,r)=>{f(n,t,e(r))}),r&&(r.finalized_=!1),n}(e)}d(S,(e,t)=>{C[e]=function(){return arguments[0]=arguments[0][0],t.apply(this,arguments)}}),C.deleteProperty=function(e,t){return C.set.call(this,e,t,void 0)},C.set=function(e,t,n){return S.set.call(this,e[0],t,n,e[0])};var N=new class{constructor(e){this.autoFreeze_=!0,this.useStrictShallowCopy_=!1,this.produce=(e,t,r)=>{let i;if("function"==typeof e&&"function"!=typeof t){let n=t;t=e;let r=this;return function(e=n,...i){return r.produce(e,e=>t.call(this,e,...i))}}if("function"!=typeof t&&a(6),void 0!==r&&"function"!=typeof r&&a(7),l(e)){let n=I(this),a=B(e,void 0),o=!0;try{i=t(a),o=!1}finally{o?P(n):j(n)}return x(n,r),R(i,n)}if(e&&"object"==typeof e)a(1,e);else{if(void 0===(i=t(e))&&(i=e),i===n&&(i=void 0),this.autoFreeze_&&y(i,!0),r){let t=[],n=[];z("Patches").generateReplacementPatches_(e,i,t,n),r(t,n)}return i}},this.produceWithPatches=(e,t)=>{let n,r;return"function"==typeof e?(t,...n)=>this.produceWithPatches(t,t=>e(t,...n)):[this.produce(e,t,(e,t)=>{n=e,r=t}),n,r]},"boolean"==typeof e?.autoFreeze&&this.setAutoFreeze(e.autoFreeze),"boolean"==typeof e?.useStrictShallowCopy&&this.setUseStrictShallowCopy(e.useStrictShallowCopy)}createDraft(e){l(e)||a(8),s(e)&&(e=D(e));let t=I(this),n=B(e,void 0);return n[i].isManual_=!0,j(t),n}finishDraft(e,t){let n=e&&e[i];n&&n.isManual_||a(9);let{scope_:r}=n;return x(r,t),R(void 0,r)}setAutoFreeze(e){this.autoFreeze_=e}setUseStrictShallowCopy(e){this.useStrictShallowCopy_=e}applyPatches(e,t){let n;for(n=t.length-1;n>=0;n--){let r=t[n];if(0===r.path.length&&"replace"===r.op){e=r.value;break}}n>-1&&(t=t.slice(n+1));let r=z("Patches").applyPatches_;return s(e)?r(e,t):this.produce(e,e=>r(e,t))}}().produce;e.s(["castDraft",0,function(e){return e},"current",0,D,"freeze",0,y,"isDraft",0,s,"isDraftable",0,l,"original",0,function(e){return s(e)||a(15,e),e[i].base_},"produce",0,N])},980533,e=>{"use strict";var t,n=e.i(554331),r=e.i(361101);e.s([],919735),e.i(919735),e.i(622621);var i=e.i(764838),a=e.i(123651),o=e.i(228876),s=e.i(235901),l=e.i(361409),u=e.i(854855),c=e.i(618568),d=e.i(281334),p=e.i(356120),m=e.i(593478),f=e.i(481902),g=e.i(397744);let h=i.createContext(void 0);var _=e.i(391699);let b=((t={}).checked="data-checked",t.unchecked="data-unchecked",t.disabled="data-disabled",t.readonly="data-readonly",t.required="data-required",t.valid="data-valid",t.invalid="data-invalid",t.touched="data-touched",t.dirty="data-dirty",t.filled="data-filled",t.focused="data-focused",t),y={..._.fieldValidityMapping,checked:e=>e?{[b.checked]:""}:{[b.unchecked]:""}};var v=e.i(761073),w=e.i(897464),E=e.i(965358),z=e.i(231152),x=e.i(459128),P=e.i(435848),j=e.i(939550),I=e.i(467219),O=e.i(412425);let R=i.forwardRef(function(e,t){let{checked:r,className:g,defaultChecked:_,"aria-labelledby":b,form:R,id:k,inputRef:$,name:A,nativeButton:S=!1,onCheckedChange:C,readOnly:T=!1,required:M=!1,disabled:F=!1,render:L,uncheckedValue:B,value:D,style:N,...q}=e,{clearErrors:U}=(0,E.useFormContext)(),{state:K,setTouched:H,setDirty:W,validityData:G,setFilled:V,setFocused:Y,shouldValidateOnChange:J,validationMode:Q,disabled:X,name:Z,validation:ee}=(0,v.useFieldRootContext)(),{labelId:et}=(0,z.useLabelableContext)(),en=X||F,er=Z??A,ei=(0,o.useStableCallback)(C),ea=i.useRef(null),eo=(0,s.useMergedRefs)(ea,$,ee.inputRef),es=i.useRef(null),el=(0,m.useBaseUiId)(),eu=(0,P.useLabelableId)({id:k,implicit:!1,controlRef:es}),ec=S?void 0:eu,[ed,ep]=(0,a.useControlled)({controlled:r,default:!!_,name:"Switch",state:"checked"});(0,w.useRegisterFieldControl)(es,{id:el,value:ed}),(0,l.useIsoLayoutEffect)(()=>{ea.current&&V(ea.current.checked)},[ea,V]),(0,O.useValueChanged)(ed,()=>{U(er),W(ed!==G.initialValue),V(ed),J()?ee.commit(ed):ee.commit(ed,!0)});let{getButtonProps:em,buttonRef:ef}=(0,f.useButton)({disabled:en,native:S}),eg=(0,x.useAriaLabelledBy)(b,et,ea,!S,ec),eh=i.useMemo(()=>(0,p.mergeProps)({checked:ed,disabled:en,form:R,id:ec,name:er,required:M,style:er?u.visuallyHiddenInput:u.visuallyHidden,tabIndex:-1,type:"checkbox","aria-hidden":!0,ref:eo,onChange(e){if(e.nativeEvent.defaultPrevented)return;if(T)return void e.preventDefault();let t=e.currentTarget.checked,n=(0,j.createChangeEventDetails)(I.REASONS.none,e.nativeEvent);ei?.(t,n),n.isCanceled||ep(t)},onFocus(){es.current?.focus()}},ee.getInputValidationProps,void 0!==D?{value:D}:c.EMPTY_OBJECT),[ed,en,R,eo,ec,er,ei,T,M,ep,ee,D]),e_=i.useMemo(()=>({...K,checked:ed,disabled:en,readOnly:T,required:M}),[K,ed,en,T,M]),eb=(0,d.useRenderElement)("span",e,{state:e_,ref:[t,es,ef],props:[{id:S?eu:el,role:"switch","aria-checked":ed,"aria-readonly":T||void 0,"aria-required":M||void 0,"aria-labelledby":eg,onFocus(){en||Y(!0)},onBlur(){let e=ea.current;e&&!en&&(H(!0),Y(!1),"onBlur"===Q&&ee.commit(e.checked))},onClick(e){T||en||(e.preventDefault(),ea.current?.dispatchEvent(new PointerEvent("click",{bubbles:!0,shiftKey:e.shiftKey,ctrlKey:e.ctrlKey,altKey:e.altKey,metaKey:e.metaKey})))}},ee.getValidationProps,q,em],stateAttributesMapping:y});return(0,n.jsxs)(h.Provider,{value:e_,children:[eb,!ed&&er&&void 0!==B&&(0,n.jsx)("input",{type:"hidden",form:R,name:er,value:B}),(0,n.jsx)("input",{...eh,suppressHydrationWarning:!0})]})}),k=i.forwardRef(function(e,t){let{render:n,className:r,style:a,...o}=e,{state:s}=(0,v.useFieldRootContext)(),l=function(){let e=i.useContext(h);if(void 0===e)throw Error((0,g.default)(63));return e}(),u={...s,...l};return(0,d.useRenderElement)("span",e,{state:u,ref:t,stateAttributesMapping:y,props:o})});e.s(["Root",0,R,"Thumb",0,k],254305);var $=e.i(254305),$=$,A=e.i(452473);let S={default:"h-6 w-11",sm:"h-5 w-9",xs:"h-3 w-5"},C={default:"h-5 w-5 data-[checked]:translate-x-5",sm:"h-4 w-4 data-[checked]:translate-x-4",xs:"h-2 w-2 data-[checked]:translate-x-2"};e.s(["Switch",0,function(e){let t,i,a,o,s,l,u=(0,r.c)(28),{className:c,size:d,checked:p,defaultChecked:m,onCheckedChange:f,disabled:g,required:h,name:_,id:b,title:y,onClick:v,ref:w,"aria-label":E,"aria-labelledby":z,"aria-describedby":x}=e,P=void 0===d?"default":d,j=S[P];u[0]!==c||u[1]!==j?(t=(0,A.cn)("peer inline-flex shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent transition-colors focus-visible:outline-none focus-visible:border-focus-border focus-visible:shadow-focus disabled:cursor-not-allowed disabled:opacity-50 data-[checked]:bg-primary data-[unchecked]:bg-foreground/30 hover:data-[unchecked]:bg-foreground/40",j,c),u[0]=c,u[1]=j,u[2]=t):t=u[2],u[3]!==f?(i=f?e=>f(e):void 0,u[3]=f,u[4]=i):i=u[4],u[5]!==E||u[6]!==z?(a=(e,t)=>{let r=z??(E?void 0:e["aria-labelledby"]);return(0,n.jsx)("button",{type:"button",...e,"data-state":t.checked?"checked":"unchecked","aria-labelledby":r})},u[5]=E,u[6]=z,u[7]=a):a=u[7];let I=C[P];return u[8]!==I?(o=(0,A.cn)("pointer-events-none block rounded-full bg-background shadow-lg ring-0 transition-transform data-[unchecked]:translate-x-0",I),u[8]=I,u[9]=o):o=u[9],u[10]!==o?(s=(0,n.jsx)($.Thumb,{className:o}),u[10]=o,u[11]=s):s=u[11],u[12]!==x||u[13]!==E||u[14]!==p||u[15]!==m||u[16]!==g||u[17]!==b||u[18]!==_||u[19]!==v||u[20]!==w||u[21]!==h||u[22]!==t||u[23]!==i||u[24]!==a||u[25]!==s||u[26]!==y?(l=(0,n.jsx)($.Root,{className:t,checked:p,defaultChecked:m,onCheckedChange:i,disabled:g,required:h,name:_,id:b,title:y,onClick:v,ref:w,"aria-label":E,"aria-describedby":x,nativeButton:!0,render:a,children:s}),u[12]=x,u[13]=E,u[14]=p,u[15]=m,u[16]=g,u[17]=b,u[18]=_,u[19]=v,u[20]=w,u[21]=h,u[22]=t,u[23]=i,u[24]=a,u[25]=s,u[26]=y,u[27]=l):l=u[27],l}],980533)},459128,e=>{"use strict";var t=e.i(764838),n=e.i(361409),r=e.i(593478);e.s(["useAriaLabelledBy",0,function(e,i,a,o=!0,s){let[l,u]=t.useState(),c=(0,r.useBaseUiId)(s?`${s}-label`:void 0),d=e??i??l;return(0,n.useIsoLayoutEffect)(()=>{let t=e||i||!o?void 0:function(e,t){let n=function(e){if(!e)return;let t=e.parentElement;if(t&&"LABEL"===t.tagName)return t;let n=e.id;if(n){let t=e.nextElementSibling;if(t&&t.htmlFor===n)return t}let r=e.labels;return r&&r[0]}(e);if(n)return!n.id&&t&&(n.id=t),n.id||void 0}(a.current,c);l!==t&&u(t)}),d}])},964610,e=>{"use strict";var t=e.i(554331),n=e.i(361101),r=e.i(452473);let i=(0,e.i(207298).cva)("text-xs font-normal leading-none text-muted-foreground peer-disabled:cursor-not-allowed peer-disabled:opacity-70");e.s(["Label",0,function(e){let a,o,s,l,u,c,d,p=(0,n.c)(14);return p[0]!==e?({className:a,ref:l,onMouseDown:o,...s}=e,p[0]=e,p[1]=a,p[2]=o,p[3]=s,p[4]=l):(a=p[1],o=p[2],s=p[3],l=p[4]),p[5]!==a?(u=(0,r.cn)(i(),a),p[5]=a,p[6]=u):u=p[6],p[7]!==o?(c=e=>{o?.(e),!e.defaultPrevented&&e.detail>1&&e.preventDefault()},p[7]=o,p[8]=c):c=p[8],p[9]!==s||p[10]!==l||p[11]!==u||p[12]!==c?(d=(0,t.jsx)("label",{ref:l,className:u,onMouseDown:c,...s}),p[9]=s,p[10]=l,p[11]=u,p[12]=c,p[13]=d):d=p[13],d}])},118674,e=>{"use strict";var t=e.i(554331),n=e.i(361101),r=e.i(452473);let i=(0,r.cn)("flex min-h-[80px] w-full px-3 py-2","rounded-md border border-input bg-input-bg text-body pointer-coarse:text-base","placeholder:text-muted-foreground/50","focus-visible:outline-hidden focus-visible:ring-0 focus-visible:border-focus-border focus-visible:shadow-focus","disabled:cursor-not-allowed disabled:opacity-50");e.s(["TEXTAREA_CLASSES",0,i,"Textarea",0,function(e){let a,o,s,l,u,c,d=(0,n.c)(12);return d[0]!==e?({className:a,inputClassName:o,ref:l,...s}=e,d[0]=e,d[1]=a,d[2]=o,d[3]=s,d[4]=l):(a=d[1],o=d[2],s=d[3],l=d[4]),d[5]!==a||d[6]!==o?(u=(0,r.cn)(i,o,a),d[5]=a,d[6]=o,d[7]=u):u=d[7],d[8]!==s||d[9]!==l||d[10]!==u?(c=(0,t.jsx)("textarea",{className:u,ref:l,...s}),d[8]=s,d[9]=l,d[10]=u,d[11]=c):c=d[11],c}])},649188,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3"}))});e.s(["ArrowDownTrayIcon",0,n],649188)},316280,(e,t,n)=>{"use strict";Object.defineProperty(n,"__esModule",{value:!0}),Object.defineProperty(n,"default",{enumerable:!0,get:function(){return s}});let r=e.r(764838),i="u"<typeof window,a=i?()=>{}:r.useLayoutEffect,o=i?()=>{}:r.useEffect;function s(e){let{headManager:t,reduceComponentsToState:n}=e;function s(){if(t&&t.mountedInstances){let e=r.Children.toArray(Array.from(t.mountedInstances).filter(Boolean));t.updateHead(n(e))}}return i&&(t?.mountedInstances?.add(e.children),s()),a(()=>(t?.mountedInstances?.add(e.children),()=>{t?.mountedInstances?.delete(e.children)})),a(()=>(t&&(t._pendingUpdate=s),()=>{t&&(t._pendingUpdate=s)})),o(()=>(t&&t._pendingUpdate&&(t._pendingUpdate(),t._pendingUpdate=null),()=>{t&&t._pendingUpdate&&(t._pendingUpdate(),t._pendingUpdate=null)})),null}},574736,(e,t,n)=>{"use strict";Object.defineProperty(n,"__esModule",{value:!0});var r={default:function(){return g},defaultHead:function(){return d}};for(var i in r)Object.defineProperty(n,i,{enumerable:!0,get:r[i]});let a=e.r(940192),o=e.r(475244),s=e.r(554331),l=o._(e.r(764838)),u=a._(e.r(316280)),c=e.r(433490);function d(){return[(0,s.jsx)("meta",{charSet:"utf-8"},"charset"),(0,s.jsx)("meta",{name:"viewport",content:"width=device-width"},"viewport")]}function p(e,t){return"string"==typeof t||"number"==typeof t?e:t.type===l.default.Fragment?e.concat(l.default.Children.toArray(t.props.children).reduce((e,t)=>"string"==typeof t||"number"==typeof t?e:e.concat(t),[])):e.concat(t)}e.r(855738);let m=["name","httpEquiv","charSet","itemProp"];function f(e){let t,n,r,i;return e.reduce(p,[]).reverse().concat(d().reverse()).filter((t=new Set,n=new Set,r=new Set,i={},e=>{let a=!0,o=!1;if(e.key&&"number"!=typeof e.key&&e.key.indexOf("$")>0){o=!0;let n=e.key.slice(e.key.indexOf("$")+1);t.has(n)?a=!1:t.add(n)}switch(e.type){case"title":case"base":n.has(e.type)?a=!1:n.add(e.type);break;case"meta":for(let t=0,n=m.length;t<n;t++){let n=m[t];if(e.props.hasOwnProperty(n))if("charSet"===n)r.has(n)?a=!1:r.add(n);else{let t=e.props[n],r=i[n]||new Set;("name"!==n||!o)&&r.has(t)?a=!1:(r.add(t),i[n]=r)}}}return a})).reverse().map((e,t)=>{let n=e.key||t;return l.default.cloneElement(e,{key:n})})}let g=function({children:e}){let t=(0,l.useContext)(c.HeadManagerContext);return(0,s.jsx)(u.default,{reduceComponentsToState:f,headManager:t,children:e})};("function"==typeof n.default||"object"==typeof n.default&&null!==n.default)&&void 0===n.default.__esModule&&(Object.defineProperty(n.default,"__esModule",{value:!0}),Object.assign(n.default,n),t.exports=n.default)},919205,(e,t,n)=>{"use strict";function r({widthInt:e,heightInt:t,blurWidth:n,blurHeight:i,blurDataURL:a,objectFit:o}){let s=n?40*n:e,l=i?40*i:t,u=s&&l?`viewBox='0 0 ${s} ${l}'`:"";return`%3Csvg xmlns='http://www.w3.org/2000/svg' ${u}%3E%3Cfilter id='b' color-interpolation-filters='sRGB'%3E%3CfeGaussianBlur stdDeviation='20'/%3E%3CfeColorMatrix values='1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 100 -1' result='s'/%3E%3CfeFlood x='0' y='0' width='100%25' height='100%25'/%3E%3CfeComposite operator='out' in='s'/%3E%3CfeComposite in2='SourceGraphic'/%3E%3CfeGaussianBlur stdDeviation='20'/%3E%3C/filter%3E%3Cimage width='100%25' height='100%25' x='0' y='0' preserveAspectRatio='${u?"none":"contain"===o?"xMidYMid":"cover"===o?"xMidYMid slice":"none"}' style='filter: url(%23b);' href='${a}'/%3E%3C/svg%3E`}Object.defineProperty(n,"__esModule",{value:!0}),Object.defineProperty(n,"getImageBlurSvg",{enumerable:!0,get:function(){return r}})},925598,(e,t,n)=>{"use strict";Object.defineProperty(n,"__esModule",{value:!0});var r={VALID_LOADERS:function(){return a},imageConfigDefault:function(){return o}};for(var i in r)Object.defineProperty(n,i,{enumerable:!0,get:r[i]});let a=["default","imgix","cloudinary","akamai","custom"],o={deviceSizes:[640,750,828,1080,1200,1920,2048,3840],imageSizes:[32,48,64,96,128,256,384],path:"/_next/image",loader:"default",loaderFile:"",domains:[],disableStaticImages:!1,minimumCacheTTL:14400,formats:["image/webp"],maximumDiskCacheSize:void 0,maximumRedirects:3,maximumResponseBody:5e7,dangerouslyAllowLocalIP:!1,dangerouslyAllowSVG:!1,contentSecurityPolicy:"script-src 'none'; frame-src 'none'; sandbox;",contentDispositionType:"attachment",localPatterns:void 0,remotePatterns:[],qualities:[75],unoptimized:!1,customCacheHandler:!1}},175544,(e,t,n)=>{"use strict";Object.defineProperty(n,"__esModule",{value:!0}),Object.defineProperty(n,"getImgProps",{enumerable:!0,get:function(){return u}}),e.r(855738);let r=e.r(879319),i=e.r(919205),a=e.r(925598),o=["-moz-initial","fill","none","scale-down",void 0];function s(e){return void 0!==e.default}function l(e){return void 0===e?e:"number"==typeof e?Number.isFinite(e)?e:NaN:"string"==typeof e&&/^[0-9]+$/.test(e)?parseInt(e,10):NaN}function u({src:e,sizes:t,unoptimized:n=!1,priority:c=!1,preload:d=!1,loading:p,className:m,quality:f,width:g,height:h,fill:_=!1,style:b,overrideSrc:y,onLoad:v,onLoadingComplete:w,placeholder:E="empty",blurDataURL:z,fetchPriority:x,decoding:P="async",layout:j,objectFit:I,objectPosition:O,lazyBoundary:R,lazyRoot:k,...$},A){var S;let C,T,M,{imgConf:F,showAltText:L,blurComplete:B,defaultLoader:D}=A,N=F||a.imageConfigDefault;if("allSizes"in N)C=N;else{let e=[...N.deviceSizes,...N.imageSizes].sort((e,t)=>e-t),t=N.deviceSizes.sort((e,t)=>e-t),n=N.qualities?.sort((e,t)=>e-t);C={...N,allSizes:e,deviceSizes:t,qualities:n}}if(void 0===D)throw Object.defineProperty(Error("images.loaderFile detected but the file is missing default export.\nRead more: https://nextjs.org/docs/messages/invalid-images-config"),"__NEXT_ERROR_CODE",{value:"E163",enumerable:!1,configurable:!0});let q=$.loader||D;delete $.loader,delete $.srcSet;let U="__next_img_default"in q;if(U){if("custom"===C.loader)throw Object.defineProperty(Error(`Image with src "${e}" is missing "loader" prop.
Read more: https://nextjs.org/docs/messages/next-image-missing-loader`),"__NEXT_ERROR_CODE",{value:"E252",enumerable:!1,configurable:!0})}else{let e=q;q=t=>{let{config:n,...r}=t;return e(r)}}if(j){"fill"===j&&(_=!0);let e={intrinsic:{maxWidth:"100%",height:"auto"},responsive:{width:"100%",height:"auto"}}[j];e&&(b={...b,...e});let n={responsive:"100vw",fill:"100vw"}[j];n&&!t&&(t=n)}let K="",H=l(g),W=l(h);if((S=e)&&"object"==typeof S&&(s(S)||void 0!==S.src)){let t=s(e)?e.default:e;if(!t.src)throw Object.defineProperty(Error(`An object should only be passed to the image component src parameter if it comes from a static image import. It must include src. Received ${JSON.stringify(t)}`),"__NEXT_ERROR_CODE",{value:"E460",enumerable:!1,configurable:!0});if(!t.height||!t.width)throw Object.defineProperty(Error(`An object should only be passed to the image component src parameter if it comes from a static image import. It must include height and width. Received ${JSON.stringify(t)}`),"__NEXT_ERROR_CODE",{value:"E48",enumerable:!1,configurable:!0});if(T=t.blurWidth,M=t.blurHeight,z=z||t.blurDataURL,K=t.src,!_)if(H||W){if(H&&!W){let e=H/t.width;W=Math.round(t.height*e)}else if(!H&&W){let e=W/t.height;H=Math.round(t.width*e)}}else H=t.width,W=t.height}let G=!c&&!d&&("lazy"===p||void 0===p);(!(e="string"==typeof e?e:K)||e.startsWith("data:")||e.startsWith("blob:"))&&(n=!0,G=!1),C.unoptimized&&(n=!0),U&&!C.dangerouslyAllowSVG&&e.split("?",1)[0].endsWith(".svg")&&(n=!0);let V=l(f),Y=Object.assign(_?{position:"absolute",height:"100%",width:"100%",left:0,top:0,right:0,bottom:0,objectFit:I,objectPosition:O}:{},L?{}:{color:"transparent"},b),J=B||"empty"===E?null:"blur"===E?`url("data:image/svg+xml;charset=utf-8,${(0,i.getImageBlurSvg)({widthInt:H,heightInt:W,blurWidth:T,blurHeight:M,blurDataURL:z||"",objectFit:Y.objectFit})}")`:`url("${E}")`,Q=o.includes(Y.objectFit)?"fill"===Y.objectFit?"100% 100%":"cover":Y.objectFit,X=J?{backgroundSize:Q,backgroundPosition:Y.objectPosition||"50% 50%",backgroundRepeat:"no-repeat",backgroundImage:J}:{},Z=function({config:e,src:t,unoptimized:n,width:i,quality:a,sizes:o,loader:s}){if(n){if(t.startsWith("/")&&!t.startsWith("//")){let e=(0,r.getDeploymentId)();if(e){let n=t.indexOf("?");if(-1!==n){let r=new URLSearchParams(t.slice(n+1));r.get("dpl")||(r.append("dpl",e),t=t.slice(0,n)+"?"+r.toString())}else t+=`?dpl=${e}`}}return{src:t,srcSet:void 0,sizes:void 0}}let{widths:l,kind:u}=function({deviceSizes:e,allSizes:t},n,r){if(r){let n=/(^|\s)(1?\d?\d)vw/g,i=[];for(let e;e=n.exec(r);)i.push(parseInt(e[2]));if(i.length){let n=.01*Math.min(...i);return{widths:t.filter(t=>t>=e[0]*n),kind:"w"}}return{widths:t,kind:"w"}}return"number"!=typeof n?{widths:e,kind:"w"}:{widths:[...new Set([n,2*n].map(e=>t.find(t=>t>=e)||t[t.length-1]))],kind:"x"}}(e,i,o),c=l.length-1;return{sizes:o||"w"!==u?o:"100vw",srcSet:l.map((n,r)=>`${s({config:e,src:t,quality:a,width:n})} ${"w"===u?n:r+1}${u}`).join(", "),src:s({config:e,src:t,quality:a,width:l[c]})}}({config:C,src:e,unoptimized:n,width:H,quality:V,sizes:t,loader:q}),ee=G?"lazy":p;return{props:{...$,loading:ee,fetchPriority:x,width:H,height:W,decoding:P,className:m,style:{...Y,...X},sizes:Z.sizes,srcSet:Z.srcSet,src:y||Z.src},meta:{unoptimized:n,preload:d||c,placeholder:E,fill:_}}}},767742,(e,t,n)=>{"use strict";Object.defineProperty(n,"__esModule",{value:!0}),Object.defineProperty(n,"ImageConfigContext",{enumerable:!0,get:function(){return a}});let r=e.r(940192)._(e.r(764838)),i=e.r(925598),a=r.default.createContext(i.imageConfigDefault)},554473,(e,t,n)=>{"use strict";function r(e,t){let n=e||75;return t?.qualities?.length?t.qualities.reduce((e,t)=>Math.abs(t-n)<Math.abs(e-n)?t:e,t.qualities[0]):n}Object.defineProperty(n,"__esModule",{value:!0}),Object.defineProperty(n,"findClosestQuality",{enumerable:!0,get:function(){return r}})},81240,(e,t,n)=>{"use strict";Object.defineProperty(n,"__esModule",{value:!0}),Object.defineProperty(n,"default",{enumerable:!0,get:function(){return o}});let r=e.r(554473),i=e.r(879319);function a({config:e,src:t,width:n,quality:o}){let s=(0,i.getDeploymentId)();if(t.startsWith("/")&&!t.startsWith("//")){let e=t.indexOf("?");if(-1!==e){let n=new URLSearchParams(t.slice(e+1)),r=n.get("dpl");if(r){s=r,n.delete("dpl");let i=n.toString();t=t.slice(0,e)+(i?"?"+i:"")}}}if(t.startsWith("/")&&t.includes("?")&&e.localPatterns?.length===1&&"**"===e.localPatterns[0].pathname&&""===e.localPatterns[0].search)throw Object.defineProperty(Error(`Image with src "${t}" is using a query string which is not configured in images.localPatterns.
Read more: https://nextjs.org/docs/messages/next-image-unconfigured-localpatterns`),"__NEXT_ERROR_CODE",{value:"E871",enumerable:!1,configurable:!0});let l=(0,r.findClosestQuality)(o,e);return`${e.path}?url=${encodeURIComponent(t)}&w=${n}&q=${l}${t.startsWith("/")&&s?`&dpl=${s}`:""}`}a.__next_img_default=!0;let o=a},476230,(e,t,n)=>{"use strict";Object.defineProperty(n,"__esModule",{value:!0}),Object.defineProperty(n,"Image",{enumerable:!0,get:function(){return v}});let r=e.r(940192),i=e.r(475244),a=e.r(554331),o=i._(e.r(764838)),s=r._(e.r(557438)),l=r._(e.r(574736)),u=e.r(175544),c=e.r(925598),d=e.r(767742);e.r(855738);let p=e.r(821104),m=r._(e.r(81240)),f=e.r(67724),g={deviceSizes:[640,750,828,1080,1200,1920,2048,3840],imageSizes:[32,48,64,96,128,256,384],qualities:[75],path:"/_next/image",loader:"default",dangerouslyAllowSVG:!1,unoptimized:!1};function h(e,t,n,r,i,a,o){let s=e?.src;e&&e["data-loaded-src"]!==s&&(e["data-loaded-src"]=s,("decode"in e?e.decode():Promise.resolve()).catch(()=>{}).then(()=>{if(e.parentElement&&e.isConnected){if("empty"!==t&&i(!0),n?.current){let t=new Event("load");Object.defineProperty(t,"target",{writable:!1,value:e});let r=!1,i=!1;n.current({...t,nativeEvent:t,currentTarget:e,target:e,isDefaultPrevented:()=>r,isPropagationStopped:()=>i,persist:()=>{},preventDefault:()=>{r=!0,t.preventDefault()},stopPropagation:()=>{i=!0,t.stopPropagation()}})}r?.current&&r.current(e)}}))}function _(e){return o.use?{fetchPriority:e}:{fetchpriority:e}}"u"<typeof window&&(globalThis.__NEXT_IMAGE_IMPORTED=!0);let b=(0,o.forwardRef)(({src:e,srcSet:t,sizes:n,height:r,width:i,decoding:s,className:l,style:u,fetchPriority:c,placeholder:d,loading:p,unoptimized:m,fill:g,onLoadRef:b,onLoadingCompleteRef:y,setBlurComplete:v,setShowAltText:w,sizesInput:E,onLoad:z,onError:x,...P},j)=>{let I=(0,o.useCallback)(e=>{e&&(x&&(e.src=e.src),e.complete&&h(e,d,b,y,v,m,E))},[e,d,b,y,v,x,m,E]),O=(0,f.useMergedRef)(j,I);return(0,a.jsx)("img",{...P,..._(c),loading:p,width:i,height:r,decoding:s,"data-nimg":g?"fill":"1",className:l,style:u,sizes:n,srcSet:t,src:e,ref:O,onLoad:e=>{h(e.currentTarget,d,b,y,v,m,E)},onError:e=>{w(!0),"empty"!==d&&v(!0),x&&x(e)}})});function y({isAppRouter:e,imgAttributes:t}){let n={as:"image",imageSrcSet:t.srcSet,imageSizes:t.sizes,crossOrigin:t.crossOrigin,referrerPolicy:t.referrerPolicy,..._(t.fetchPriority)};return e&&s.default.preload?(s.default.preload(t.src,n),null):(0,a.jsx)(l.default,{children:(0,a.jsx)("link",{rel:"preload",href:t.srcSet?void 0:t.src,...n},"__nimg-"+t.src+t.srcSet+t.sizes)})}let v=(0,o.forwardRef)((e,t)=>{let n=(0,o.useContext)(p.RouterContext),r=(0,o.useContext)(d.ImageConfigContext),i=(0,o.useMemo)(()=>{let e=g||r||c.imageConfigDefault,t=[...e.deviceSizes,...e.imageSizes].sort((e,t)=>e-t),n=e.deviceSizes.sort((e,t)=>e-t),i=e.qualities?.sort((e,t)=>e-t);return{...e,allSizes:t,deviceSizes:n,qualities:i,localPatterns:"u"<typeof window?r?.localPatterns:e.localPatterns}},[r]),{onLoad:s,onLoadingComplete:l}=e,f=(0,o.useRef)(s);(0,o.useEffect)(()=>{f.current=s},[s]);let h=(0,o.useRef)(l);(0,o.useEffect)(()=>{h.current=l},[l]);let[_,v]=(0,o.useState)(!1),[w,E]=(0,o.useState)(!1),{props:z,meta:x}=(0,u.getImgProps)(e,{defaultLoader:m.default,imgConf:i,blurComplete:_,showAltText:w});return(0,a.jsxs)(a.Fragment,{children:[(0,a.jsx)(b,{...z,unoptimized:x.unoptimized,placeholder:x.placeholder,fill:x.fill,onLoadRef:f,onLoadingCompleteRef:h,setBlurComplete:v,setShowAltText:E,sizesInput:e.sizes,ref:t}),x.preload?(0,a.jsx)(y,{isAppRouter:!n,imgAttributes:z}):null]})});("function"==typeof n.default||"object"==typeof n.default&&null!==n.default)&&void 0===n.default.__esModule&&(Object.defineProperty(n.default,"__esModule",{value:!0}),Object.assign(n.default,n),t.exports=n.default)},17805,(e,t,n)=>{"use strict";Object.defineProperty(n,"__esModule",{value:!0});var r={default:function(){return c},getImageProps:function(){return u}};for(var i in r)Object.defineProperty(n,i,{enumerable:!0,get:r[i]});let a=e.r(940192),o=e.r(175544),s=e.r(476230),l=a._(e.r(81240));function u(e){let{props:t}=(0,o.getImgProps)(e,{defaultLoader:l.default,imgConf:{deviceSizes:[640,750,828,1080,1200,1920,2048,3840],imageSizes:[32,48,64,96,128,256,384],qualities:[75],path:"/_next/image",loader:"default",dangerouslyAllowSVG:!1,unoptimized:!1}});for(let[e,n]of Object.entries(t))void 0===n&&delete t[e];return{props:t}}let c=s.Image},613109,(e,t,n)=>{t.exports=e.r(17805)},704735,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"m6.75 7.5 3 2.25-3 2.25m4.5 0h3m-9 8.25h13.5A2.25 2.25 0 0 0 21 18V6a2.25 2.25 0 0 0-2.25-2.25H5.25A2.25 2.25 0 0 0 3 6v12a2.25 2.25 0 0 0 2.25 2.25Z"}))});e.s(["CommandLineIcon",0,n],704735)},613889,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M17.25 6.75 22.5 12l-5.25 5.25m-10.5 0L1.5 12l5.25-5.25m7.5-3-4.5 16.5"}))});e.s(["CodeBracketIcon",0,n],613889)},235856,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z"}))});e.s(["DocumentTextIcon",0,n],235856)},267064,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 24 24",fill:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{fillRule:"evenodd",d:"M11.47 2.47a.75.75 0 0 1 1.06 0l7.5 7.5a.75.75 0 1 1-1.06 1.06l-6.22-6.22V21a.75.75 0 0 1-1.5 0V4.81l-6.22 6.22a.75.75 0 1 1-1.06-1.06l7.5-7.5Z",clipRule:"evenodd"}))});e.s(["default",0,n])},379497,e=>{"use strict";var t=e.i(222584);e.s(["ChevronRight",()=>t.default])},607296,e=>{"use strict";let t=(0,e.i(202913).default)("chevron-left",[["path",{d:"m15 18-6-6 6-6",key:"1wnfg3"}]]);e.s(["ChevronLeft",0,t],607296)},376100,e=>{"use strict";var t=e.i(204067),n=e.i(868280);let r={VideoGeneration:"video_generation",Batch:"batch"},i={Pending:"pending",InProgress:"in_progress",Completed:"completed",Failed:"failed",Cancelled:"cancelled",Expired:"expired"};i.Pending,i.InProgress,n.z.object({billable_entity_id:n.z.string(),workspace_id:n.z.string().optional(),job_type:n.z.nativeEnum(r),job_id:n.z.string(),model:n.z.string().optional(),provider_name:n.z.string().optional(),status:n.z.nativeEnum(i),provider_job_id:n.z.string().optional(),callback_url:n.z.string().optional(),estimated_cost:n.z.string(),is_byok:n.z.boolean().optional(),started_at:n.z.string(),api_key_id:(0,t.zInt)().optional(),provider_api_key_id:(0,t.zInt)().optional(),creator_user_id:n.z.string().optional(),credit_pool_id:n.z.string().optional(),result:n.z.unknown().optional(),generation_id:n.z.string().optional(),usage:n.z.record(n.z.string(),n.z.unknown()).optional(),request_id:n.z.string().optional(),api_path:n.z.string().optional(),endpoint_id:n.z.string().optional(),input_gcs_uri:n.z.string().optional(),output_gcs_uri:n.z.string().optional(),total_request_count:(0,t.zInt)().nonnegative().optional(),succeeded_request_count:(0,t.zInt)().nonnegative().optional(),failed_request_count:(0,t.zInt)().nonnegative().optional(),cancelled_request_count:(0,t.zInt)().nonnegative().optional(),completion_window:n.z.string().optional(),expires_at:n.z.string().optional(),upstream_input_file_id:n.z.string().optional(),upstream_output_file_id:n.z.string().optional()}),Object.keys(n.z.object({job_id:n.z.string(),billable_entity_id:n.z.string(),workspace_id:n.z.string().nullish(),status:n.z.nativeEnum(i),result:n.z.unknown(),provider_name:n.z.string().nullable(),model:n.z.string().nullable(),provider_job_id:n.z.string().nullable(),generation_id:n.z.string().nullable(),usage:n.z.record(n.z.string(),n.z.unknown()).nullable(),provider_api_key_id:n.z.coerce.number().int().nullable(),updated_at:n.z.string(),request_id:n.z.string().nullable(),api_path:n.z.string().nullable(),endpoint_id:n.z.string().nullable(),input_gcs_uri:n.z.string().nullable(),output_gcs_uri:n.z.string().nullable(),total_request_count:n.z.coerce.number().int().nonnegative().nullable(),succeeded_request_count:n.z.coerce.number().int().nonnegative().nullable(),failed_request_count:n.z.coerce.number().int().nonnegative().nullable(),cancelled_request_count:n.z.coerce.number().int().nonnegative().nullable(),completion_window:n.z.string().nullable(),expires_at:n.z.string().nullable(),upstream_input_file_id:n.z.string().nullable(),upstream_output_file_id:n.z.string().nullable()}).shape).join(", "),n.z.object({billable_entity_id:n.z.string(),job_id:n.z.string(),job_type:n.z.string(),model:n.z.string().nullable(),provider_name:n.z.string().nullable(),status:n.z.nativeEnum(i),started_at:n.z.string(),inserted_at:n.z.string(),updated_at:n.z.string(),estimated_cost:n.z.string().nullable(),usage:n.z.record(n.z.string(),n.z.unknown()).nullable(),provider_job_id:n.z.string().nullable(),generation_id:n.z.string().nullable(),result:n.z.unknown(),request_id:n.z.string().nullable(),api_path:n.z.string().nullable(),endpoint_id:n.z.string().nullable(),input_gcs_uri:n.z.string().nullable(),output_gcs_uri:n.z.string().nullable(),total_request_count:n.z.coerce.number().int().nonnegative().nullable(),succeeded_request_count:n.z.coerce.number().int().nonnegative().nullable(),failed_request_count:n.z.coerce.number().int().nonnegative().nullable(),cancelled_request_count:n.z.coerce.number().int().nonnegative().nullable(),completion_window:n.z.string().nullable(),expires_at:n.z.string().nullable(),upstream_input_file_id:n.z.string().nullable(),upstream_output_file_id:n.z.string().nullable()});let a=n.z.object({job_id:n.z.string(),job_type:n.z.string(),model:n.z.string().nullable(),provider_name:n.z.string().nullable(),status:n.z.nativeEnum(i),started_at:n.z.string(),estimated_cost:(0,t.zDouble)().nullable(),usage:(0,t.zDouble)().nullable(),generation_id:n.z.string().nullable(),error_message:n.z.string().nullable(),result_urls:n.z.array(n.z.string()).nullable(),request_id:n.z.string().nullable(),total_request_count:n.z.number().int().nonnegative().nullable(),succeeded_request_count:n.z.number().int().nonnegative().nullable(),failed_request_count:n.z.number().int().nonnegative().nullable(),cancelled_request_count:n.z.number().int().nonnegative().nullable(),completion_window:n.z.string().nullable(),expires_at:n.z.string().nullable()});n.z.object({data:n.z.array(a)});let o=n.z.object({total_estimated_cost:(0,t.zDouble)(),in_flight_async_job_count:n.z.number().int().nonnegative().optional()});n.z.object({data:o}),e.s(["AsyncJobStatus",0,i,"AsyncJobType",0,r])},82544,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"m4.5 15.75 7.5-7.5 7.5 7.5"}))});e.s(["ChevronUpIcon",0,n],82544)},159119,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z"}))});e.s(["DocumentIcon",0,n],159119)},184421,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5m-13.5-9L12 3m0 0 4.5 4.5M12 3v13.5"}))});e.s(["ArrowUpTrayIcon",0,n],184421)},614991,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"}))});e.s(["PhotoIcon",0,n],614991)},492009,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"m15.75 10.5 4.72-4.72a.75.75 0 0 1 1.28.53v11.38a.75.75 0 0 1-1.28.53l-4.72-4.72M4.5 18.75h9a2.25 2.25 0 0 0 2.25-2.25v-9a2.25 2.25 0 0 0-2.25-2.25h-9A2.25 2.25 0 0 0 2.25 7.5v9a2.25 2.25 0 0 0 2.25 2.25Z"}))});e.s(["VideoCameraIcon",0,n],492009)},674026,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M8.25 9V5.25A2.25 2.25 0 0 1 10.5 3h6a2.25 2.25 0 0 1 2.25 2.25v13.5A2.25 2.25 0 0 1 16.5 21h-6a2.25 2.25 0 0 1-2.25-2.25V15M12 9l3 3m0 0-3 3m3-3H2.25"}))});e.s(["ArrowRightEndOnRectangleIcon",0,n],674026)},860816,e=>{"use strict";function t(e,n={baseIndent:0}){let r=e.split("\n"),i=r.map(e=>e.length-e.trimStart().length).filter(e=>e>0),a=Math.min(...i)-n.baseIndent,o=Math.max(n.baseIndent-Math.min(...i),0);return r.map((e,t)=>{let n=e.length-e.trimStart().length;return o>0&&t>0?" ".repeat(o)+e:n>=a?e.substring(a):e}).join("\n")}function n(e,t=2){try{return JSON.stringify(e,null,t)}catch{return String(e)}}function r(e,t=2){return n(e,t)}function i(e,r=8){return t(n(e),{baseIndent:r})}e.s(["getIndentation",0,function(e=8){return" ".repeat(e)},"indentObjectParam",0,i,"indentObjectParamForCode",0,function(e,t=8){return r(e)},"indentObjectParamPython",0,function(e,t=8){return i(e,t).replaceAll(/: true(?=\s|,|}|$)/gm,": True").replaceAll(/: false(?=\s|,|}|$)/gm,": False").replaceAll(/: null(?=\s|,|}|$)/gm,": None")},"normalizeIndentation",0,t,"prettyJson",0,n,"prettyJsonForCode",0,r])},24469,e=>{"use strict";var t=e.i(515213);e.s(["useSWR",()=>t.default])},364933,e=>{"use strict";var t=e.i(442427),n=e.i(860816);let r="<MODEL_ID>",i="<YOUR_SITE_URL>",a="<YOUR_SITE_NAME>",o="//";function s(e,...t){return e.reduce((e,n,r)=>{let i=t[r];return i?`${e}${n}${i}`:`${e}${n}`.trimEnd()},"")}let l=({siteUrl:e=i,siteName:t=a,commentPrefix:n=o}={})=>[`"HTTP-Referer": "${e}", ${n} Optional. Site URL for rankings on openrouter.ai.`,`"X-OpenRouter-Title": "${t}", ${n} Optional. Site title for rankings on openrouter.ai.`];e.s(["SITE_NAME_REF",0,a,"SITE_URL_REF",0,i,"getCURLExample",0,({apiKey:e="$OPENROUTER_API_KEY",data:t="",endpoint:n="chat/completions"})=>`
  curl https://openrouter.ai/api/v1/${n} \\
    -H "Content-Type: application/json" \\
    -H "Authorization: Bearer ${e}" \\
    -d '${t}'
`,"getFetchExample",0,({apiKey:e=t.API_KEY_REF,siteUrl:u=i,siteName:c=a,model:d=r,system:p="",prompt:m="Hello",messages:f="",prefill:g="",top_p:h,temperature:_,frequency_penalty:b,presence_penalty:y,repetition_penalty:v,provider:w,top_k:E,response_format:z})=>{let x=f;x&&0!==x.length||(x=[p&&`{"role": "system", "content": "${p}"}`,`{"role": "user", "content": "${m}"}`,g&&`{"role": "assistant", "content": "${g}"}`].filter(Boolean).join(",\n      "),x=`[
        ${x}
      ]`);let P=`"${r}", ${o} Required. ex: "openai/gpt-4o"`,j=[`"model": ${!d||d===r?P:`"${d}"`}`,`"messages": ${x}`,h&&`"top_p": ${h}`,_&&`"temperature": ${_}`,b&&`"frequency_penalty": ${b}`,y&&`"presence_penalty": ${y}`,v&&`"repetition_penalty": ${v}`,E&&`"top_k": ${E}`,w&&`"provider": ${(0,n.indentObjectParam)(w)}`,z&&`"response_format": ${(0,n.indentObjectParam)(z)}`].filter(Boolean).join(`,
${(0,n.getIndentation)(6)}`);return s`
  fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": "Bearer ${e}",
      ${l({siteUrl:u,siteName:c}).join("\n      ")}
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      ${j}
    })
  });
`},"getHeaderLines",0,l])},748700,e=>{"use strict";e.i(204067);var t=e.i(868280);let n={Enum:"enum",Range:"range",Boolean:"boolean"},r=t.z.object({type:t.z.literal(n.Enum),values:t.z.array(t.z.string())}).openapi("EnumCapability",{description:"A parameter that accepts one of a discrete set of string values.",example:{type:"enum",values:["1K","2K","4K"]}}),i=t.z.object({type:t.z.literal(n.Range),min:t.z.number(),max:t.z.number()}).openapi("RangeCapability",{description:"A parameter that accepts any value within an inclusive numeric range.",example:{type:"range",min:0,max:100}}),a=t.z.object({type:t.z.literal(n.Boolean)}).openapi("BooleanCapability",{description:"A supported-or-not flag. Present means the parameter is accepted.",example:{type:"boolean"}}),o=t.z.discriminatedUnion("type",[r,i,a]).openapi("CapabilityDescriptor",{description:"A typed descriptor for one supported request parameter.",example:{type:"enum",values:["1K","2K","4K"]},discriminator:{propertyName:"type",mapping:{enum:"#/components/schemas/EnumCapability",range:"#/components/schemas/RangeCapability",boolean:"#/components/schemas/BooleanCapability"}}}),s=t.z.record(t.z.string(),o).openapi("SupportedParameters",{description:"Supported request parameters, keyed by request field name. An absent key means the parameter is not supported.",example:{resolution:{type:"enum",values:["1K","2K","4K"]},output_compression:{type:"range",min:0,max:100},seed:{type:"boolean"}}});e.s(["CapabilityType",0,n,"SupportedParametersSchema",0,s])},971453,e=>{"use strict";var t=e.i(748700);e.s(["mergeSupportedParameters",0,function(e){let n={};for(let o of e)for(let[e,s]of Object.entries(o)){var r,i,a;let o=n[e];if(!o){n[e]=(r=s).type===t.CapabilityType.Enum?{type:t.CapabilityType.Enum,values:[...r.values]}:{...r};continue}o.type===s.type&&(n[e]=(i=o,a=s,i.type===t.CapabilityType.Enum&&a.type===t.CapabilityType.Enum?{type:t.CapabilityType.Enum,values:[...new Set([...i.values,...a.values])]}:i.type===t.CapabilityType.Range&&a.type===t.CapabilityType.Range?{type:t.CapabilityType.Range,min:Math.min(i.min,a.min),max:Math.max(i.max,a.max)}:i))}return n}])},182657,e=>{"use strict";e.s(["QuickStartExampleType",0,{Text:"text",ComputerUseTool:"computer_use_tool",AudioTool:"audio_tool",AudioOutput:"audio_output",FastApply:"fast_apply",Embeddings:"embeddings",ImageInputEmbeddings:"image_input_embeddings",Reasoning:"reasoning",ImageGeneration:"image_generation",ImageGenerationWithoutText:"image_generation_without_text",VideoGeneration:"video_generation",Rerank:"rerank",TTS:"tts",STT:"stt",OCR:"ocr"}])},543508,e=>{"use strict";var t=e.i(963),n=e.i(182657);let r="https://openrouter.ai/api/v1/chat/completions",i="https://openrouter.ai/api/v1/responses",a="https://openrouter.ai/api/v1/messages",o="/api/v1/images",s=`https://openrouter.ai${o}`,l={endpoint:r},u={endpoint:i,docsHref:"/docs/api/api-reference/responses/create-responses"},c=[l,u,{endpoint:a,docsHref:"/docs/api/api-reference/anthropic-messages/create-messages"}],d=[l,u],p=[l],m=[[t.OutputModality.Embeddings,"https://openrouter.ai/api/v1/embeddings"],[t.OutputModality.Rerank,"https://openrouter.ai/api/v1/rerank"],[t.OutputModality.TTS,"https://openrouter.ai/api/v1/audio/speech"],[t.OutputModality.Transcription,"https://openrouter.ai/api/v1/audio/transcriptions"],[t.OutputModality.Video,"https://openrouter.ai/api/v1/videos"],[t.OutputModality.Image,s]];n.QuickStartExampleType.Embeddings,n.QuickStartExampleType.ImageInputEmbeddings,n.QuickStartExampleType.VideoGeneration,n.QuickStartExampleType.Rerank,n.QuickStartExampleType.TTS,n.QuickStartExampleType.STT;let f=[{endpoint:s,docsHref:"/docs/features/multimodal/image-generation"}];e.s(["CHAT_COMPLETIONS_ENDPOINT",0,r,"IMAGE_API_ENDPOINT",0,s,"IMAGE_API_ROUTE",0,o,"MESSAGES_ENDPOINT",0,a,"RESPONSES_ENDPOINT",0,i,"getEndpointReferencesForOutputModalities",0,function(e,n){if(e.includes(t.OutputModality.Text))return c;if(e.includes(t.OutputModality.Image))return n?.useImageApi?f:d;if(e.includes(t.OutputModality.Audio))return p;let r=m.find(([t])=>e.includes(t))?.[1];return r?[{endpoint:r}]:[]}])},917138,e=>{"use strict";var t=e.i(361101),n=e.i(24469),r=e.i(748700),i=e.i(971453),a=e.i(693697),o=e.i(204067),s=e.i(868280),l=e.i(543508);let u=s.z.object({id:s.z.string(),endpoints:s.z.array(s.z.object({provider_name:s.z.string(),supported_parameters:r.SupportedParametersSchema,supports_streaming:s.z.boolean().default(!1),allowed_passthrough_parameters:s.z.array(s.z.string()).default([])}))});async function c(e){var t;let n,[,r,s]=e,c=await fetch(`${l.IMAGE_API_ROUTE}/models/${encodeURIComponent(r)}/${encodeURIComponent(s)}/endpoints`);if(!c.ok)throw c.body?.cancel(),Error(`Image discovery request failed: ${c.status} ${c.statusText}`);let d=await c.json(),p=(0,o.parseSchema)(u,d);if((0,a.isErr)(p))throw p.error;return n=(t=p.data.endpoints).map(e=>e.supported_parameters),{supportedParameters:(0,i.mergeSupportedParameters)(n),supportsStreaming:t.some(e=>e.supports_streaming),passthroughByProvider:function(e){let t=new Map;for(let n of e){let e=t.get(n.provider_name)??new Set;for(let t of n.allowed_passthrough_parameters)e.add(t);t.set(n.provider_name,e)}return[...t.entries()].filter(([,e])=>e.size>0).map(([e,t])=>({providerName:e,parameters:[...t]}))}(t)}}e.s(["useImageDiscovery",0,function(e){let r,i,a,o,s=(0,t.c)(9);s[0]!==e?(r=e.split("/"),s[0]=e,s[1]=r):r=s[1];let l=r,u=l[0],d=l[1];s[2]!==u||s[3]!==d?(i=u&&d?["image-discovery",u,d]:null,s[2]=u,s[3]=d,s[4]=i):i=s[4],s[5]===Symbol.for("react.memo_cache_sentinel")?(a={revalidateOnFocus:!1},s[5]=a):a=s[5];let{data:p,isLoading:m}=(0,n.useSWR)(i,c,a);return s[6]!==p||s[7]!==m?(o={data:p,isLoading:m},s[6]=p,s[7]=m,s[8]=o):o=s[8],o}])},449242,e=>{"use strict";var t=e.i(963),n=e.i(182657);let r={ChatCompletions:"chat-completions",ImageApi:"image-api"};e.s(["API_TAB",0,r,"getApiTabForOutputModalities",0,function(e){return e?.includes(t.OutputModality.Image)?r.ImageApi:r.ChatCompletions},"getOutputModalitiesForApiTab",0,function(e){switch(e){case r.ChatCompletions:return null;case r.ImageApi:return[t.OutputModality.Image];default:return null}},"isImageOnlyModel",0,function({quickStartExampleType:e,outputModalities:r}){return e===n.QuickStartExampleType.ImageGenerationWithoutText||e===n.QuickStartExampleType.ImageGeneration&&!r.includes(t.OutputModality.Text)}])},572729,517329,e=>{"use strict";var t=e.i(442427),n=e.i(860816),r=e.i(364933),i=e.i(963);let a=(e,t=16)=>(0,i.isTextOnly)(e)?s(t):l(e,t),o=(e=16)=>s(e),s=e=>{let t=[{role:"user",content:u}];return(0,n.indentObjectParam)(t,e).replace(/\n$/,"")},l=(e,t)=>{let r=d(e);return(0,n.indentObjectParam)([{role:"user",content:r}],t).replace(/\n$/,"")},u="What is the meaning of life?";function c(e){let t=[];for(let n of e)switch(n){case i.InputModality.Image:t.push("image");break;case i.InputModality.Video:t.push("video");break;case i.InputModality.Audio:t.push("audio");case i.InputModality.Text:case i.InputModality.File:}if(0===t.length)return u;if(1===t.length)return`What is in this ${t[0]}?`;let n=t.pop();return`What is in this ${t.join(", ")} and ${n}?`}let d=e=>{let t=[];for(let n of(t.push({type:"text",text:c(e)}),e))switch(n){case i.InputModality.Image:t.push({type:"image_url",image_url:{url:"https://live.staticflickr.com/3851/14825276609_098cac593d_b.jpg"}});break;case i.InputModality.Video:t.push({type:"video_url",video_url:{url:"https://storage.googleapis.com/cloud-samples-data/video/JaneGoodall.mp4"}});break;case i.InputModality.Audio:t.push({type:"input_audio",input_audio:{data:"UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB",format:"wav"}});case i.InputModality.Text:case i.InputModality.File:}return t};e.s(["getDefaultPromptText",0,c,"getMessagesExample",0,a,"getSdkMessagesExample",0,(e,t=16)=>{if((0,i.isTextOnly)(e))return s(t);let r=d(e).map(e=>{switch(e.type){case"text":default:return e;case"image_url":return{type:"image_url",imageUrl:e.image_url};case"video_url":case"input_video":return{type:"video_url",videoUrl:e.video_url};case"input_audio":return{type:"input_audio",inputAudio:e.input_audio}}});return(0,n.indentObjectParam)([{role:"user",content:r}],t).replace(/\n$/,"")},"getTextOnlyMessagesExample",0,o],517329),e.s(["getChatCompletionExamples",0,({slug:e,inputModalities:i,provider:s})=>[{title:"curl",language:"shell",code:(0,r.getCURLExample)({data:function({slug:e,inputModalities:t,provider:r}){return`{
    "model": "${e}",
    "messages": ${a(t,6).trimStart()}${r?`,
    "provider": ${(0,n.indentObjectParam)(r,6).trimStart()}`:""}
  }`}({slug:e,inputModalities:i,provider:s})})},{title:"openrouter-ts",language:"typescript",code:(0,n.normalizeIndentation)(`
import { OpenRouter } from "@openrouter/sdk";

const openrouter = new OpenRouter({
  apiKey: "${t.API_KEY_REF}"
});

const response = await openrouter.chat.send({
  model: "${e}",
  messages: ${a(i,4)}${s?`,
  provider: ${(0,n.indentObjectParam)(s,4)}`:""}
});

console.log(response.choices[0].message.content);
      `,{baseIndent:8})},{title:"openrouter-python",language:"python",code:(0,n.normalizeIndentation)(`
from openrouter import OpenRouter
import os

with OpenRouter(
  api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
  response = client.chat.send(
    model="${e}",
    messages=${a(i,6)}${s?`,
    provider=${(0,n.indentObjectParamPython)(s,6)}`:""}
  )

  print(response.choices[0].message.content)
      `,{baseIndent:8})},{title:"openrouter-go",language:"go",code:(0,n.normalizeIndentation)(`
package main

import (
  "context"
  "fmt"
  "os"
  openrouter "github.com/OpenRouterTeam/go-sdk"
  "github.com/OpenRouterTeam/go-sdk/models/components"
  "log"
)

func main() {
  ctx := context.Background()

  s := openrouter.New(
    openrouter.WithSecurity(os.Getenv("OPENROUTER_API_KEY")),
  )

  res, err := s.Chat.Send(ctx, components.ChatRequest{
    Messages: []components.ChatMessages{
      components.CreateChatMessagesUser(
        components.ChatUserMessage{
          Content: components.CreateChatUserMessageContentStr(
            "What is the meaning of life?",
          ),
          Role: components.ChatUserMessageRoleUser,
        },
      ),
    },
    Model: openrouter.Pointer("${e}"),
  })
  if err != nil {
    log.Fatal(err)
  }
  if res.ChatResult != nil {
    fmt.Println(res.ChatResult.Choices[0].Message.Content)
  }
}
      `,{baseIndent:8})},{title:"openai-ts",language:"typescript",code:`
        import OpenAI from 'openai';

        const openai = new OpenAI({
          baseURL: "https://openrouter.ai/api/v1",
          apiKey: "${t.API_KEY_REF}",
          defaultHeaders: {
            ${(0,r.getHeaderLines)({}).join("\n            ")}
          },
        });

        async function main() {
          const completion = await openai.chat.completions.create({
            model: "${e}",
            messages: ${a(i,14)}${s?`,
            provider: ${(0,n.indentObjectParam)(s,14)}`:""}
          });

          console.log(completion.choices[0].message);
        }

        main();
      `},{title:"openai-python",language:"python",code:(0,n.normalizeIndentation)(`
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="${t.API_KEY_REF}",
)

completion = client.chat.completions.create(
  extra_headers={
    ${(0,r.getHeaderLines)({commentPrefix:"#"}).join("\n    ")}
  },
  extra_body=${s?`${(0,n.indentObjectParamPython)({provider:s},4)}`:"{}"},
  model="${e}",
  messages=${a(i,4)}
)
print(completion.choices[0].message.content)
      `,{baseIndent:8})},{title:"anthropic-ts",language:"typescript",code:(0,n.normalizeIndentation)(`
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: "${t.API_KEY_REF}",
});

const message = await anthropic.messages.create({
  model: "${e}",
  max_tokens: 1024,
  messages: ${o(4)}
});

console.log(message.content);
      `,{baseIndent:8})},{title:"anthropic-go",language:"go",code:(0,n.normalizeIndentation)(`
package main

import (
  "context"
  "fmt"
  "os"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithBaseURL("https://openrouter.ai/api/v1"),
    option.WithAPIKey(os.Getenv("OPENROUTER_API_KEY")),
  )

  message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
    Model:     "${e}",
    MaxTokens: 1024,
    Messages: []anthropic.MessageParam{
      anthropic.NewUserMessage(
        anthropic.NewTextBlock("What is the meaning of life?"),
      ),
    },
  })
  if err != nil {
    panic(err)
  }

  fmt.Println(message.Content)
}
      `,{baseIndent:8})},{title:"python",language:"python",code:`
        import requests
        import json

        response = requests.post(
          url="https://openrouter.ai/api/v1/chat/completions",
          headers={
            "Authorization": "Bearer ${t.API_KEY_REF}",
            "Content-Type": "application/json",
            ${(0,r.getHeaderLines)({commentPrefix:"#"}).join("\n            ")}
          },
          data=json.dumps({
            "model": "${e}",
            "messages": ${a(i,14)}${s?`,
            "provider": ${(0,n.indentObjectParamPython)(s,14)}`:""}
          })
        )
      `},{title:"typescript",language:"typescript",code:(0,r.getFetchExample)({model:e,messages:a(i,8),provider:s})}]],572729)},852413,e=>{"use strict";var t=e.i(442427),n=e.i(860816),r=e.i(543508);let i=["resolution","aspect_ratio","quality","background","output_format","stream"],a="A serene mountain landscape at sunset with dramatic clouds";function o(e,t){if(0===e.length)return"";let n=e.map(({key:e,value:n})=>{var r;let i="quoted"===t.keyFormat?`"${e}"`:e;return`${t.indent}${i}: ${r=n,"python"===t.valueFormat&&"boolean"==typeof r?r?"True":"False":JSON.stringify(r)}`});return`,
${n.join(",\n")}`}e.s(["DEDICATED_IMAGE_API_PROMPT",0,a,"getDedicatedImageApiExamples",0,({slug:e,parameters:s})=>{var l;let u=(l=s,i.flatMap(e=>{let t=l?.[e];return void 0===t?[]:[{key:e,value:t}]})),c=o(u,{indent:"    ",keyFormat:"quoted",valueFormat:"json"}),d=o(u,{indent:"    ",keyFormat:"bare",valueFormat:"json"}),p=o(u,{indent:"    ",keyFormat:"quoted",valueFormat:"python"});return[{title:"curl",language:"shell",code:`curl ${r.IMAGE_API_ENDPOINT} \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \\
  -d '{
    "model": "${e}",
    "prompt": "${a}"${c}
  }'`},{title:"typescript",language:"typescript",code:(0,n.normalizeIndentation)(`
const response = await fetch("${r.IMAGE_API_ENDPOINT}", {
  method: "POST",
  headers: {
    "Authorization": "Bearer ${t.API_KEY_REF}",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "${e}",
    prompt: "${a}"${d},
  }),
});

const result = await response.json();
for (const image of result.data ?? []) {
  console.log("Image (base64):", image.b64_json.substring(0, 50) + "...");
}
      `,{baseIndent:8})},{title:"python",language:"python",code:(0,n.normalizeIndentation)(`
import requests
import json
import base64

response = requests.post(
  url="${r.IMAGE_API_ENDPOINT}",
  headers={
    "Authorization": "Bearer ${t.API_KEY_REF}",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "${e}",
    "prompt": "${a}"${p}
  })
)

result = response.json()
for i, image in enumerate(result.get("data", [])):
  image_bytes = base64.b64decode(image["b64_json"])
  with open(f"output_{i}.png", "wb") as f:
    f.write(image_bytes)
  print(f"Saved image {i + 1}")
      `,{baseIndent:8})}]}])},86575,e=>{"use strict";let t={OpenRouter:"openrouter",OpenAI:"openai",Anthropic:"anthropic",Raw:"raw"};function n(e){return e.startsWith("openrouter-")||"@openrouter/sdk"===e?t.OpenRouter:e.startsWith("openai-")||"openai-ts"===e?t.OpenAI:e.startsWith("anthropic-")?t.Anthropic:t.Raw}let r=[t.OpenRouter,t.OpenAI,t.Anthropic,t.Raw];e.s(["SDK_CATEGORY",0,t,"getCategoryForTitle",0,n,"getLanguageLabel",0,function(e){return e.endsWith("-ts")||e.endsWith("-typescript")||"@openrouter/sdk"===e?"TypeScript":e.endsWith("-python")?"Python":e.endsWith("-go")?"Go":"python"===e?"Python (requests)":"typescript"===e?"TypeScript (fetch)":"curl"===e?"cURL":e},"groupIntoCategoryTabs",0,function(e){let i=new Map;for(let t of e){let e=n(t.title),r=i.get(e);r?r.push(t):i.set(e,[t])}return r.filter(e=>i.has(e)).map(e=>({id:e,label:function(e){switch(e){case t.OpenRouter:return"OpenRouter SDK";case t.OpenAI:return"OpenAI SDK";case t.Anthropic:return"Anthropic SDK";case t.Raw:return"Raw"}}(e),examples:i.get(e)??[]}))}])},209232,186101,e=>{"use strict";var t=e.i(442427),n=e.i(860816),r=e.i(220988),i=e.i(364933);e.s(["getSttExamples",0,({slug:e})=>[{title:"python",language:"python",code:(0,n.normalizeIndentation)(`
import requests
import base64
import json

with open("audio.wav", "rb") as f:
  base64_audio = base64.b64encode(f.read()).decode("utf-8")

response = requests.post(
  url="https://openrouter.ai/api/v1/audio/transcriptions",
  headers={
    "Authorization": "Bearer ${t.API_KEY_REF}",
    "Content-Type": "application/json",
    ${(0,i.getHeaderLines)({commentPrefix:"#"}).join("\n    ")}
  },
  data=json.dumps({
    "model": "${e}",
    "input_audio": {
      "data": base64_audio,
      "format": "wav"
    }
  })
)

result = response.json()
print(result["text"])
      `,{baseIndent:8})},{title:"typescript",language:"typescript",code:`
        import fs from "fs";

        const audioBuffer = await fs.promises.readFile("audio.wav");
        const base64Audio = audioBuffer.toString("base64");

        const response = await fetch("https://openrouter.ai/api/v1/audio/transcriptions", {
          method: "POST",
          headers: {
            "Authorization": \`Bearer \${${t.API_KEY_REF}}\`,
            "Content-Type": "application/json",
            ${(0,i.getHeaderLines)({siteUrl:i.SITE_URL_REF,siteName:i.SITE_NAME_REF}).join("\n            ")}
          },
          body: JSON.stringify({
            model: "${e}",
            input_audio: {
              data: base64Audio,
              format: "wav"
            }
          })
        });

        const result = await response.json();
        console.log(result.text);
      `},{title:"curl",language:"shell",code:r.default`
        # Base64-encode your audio file
        AUDIO_BASE64=$(base64 < audio.wav | tr -d '\\n')

        curl https://openrouter.ai/api/v1/audio/transcriptions \\
          -H "Content-Type: application/json" \\
          -H "Authorization: Bearer $OPENROUTER_API_KEY" \\
          -d '{
            "model": "${e}",
            "input_audio": {
              "data": "'"$AUDIO_BASE64"'",
              "format": "wav"
            }
          }'
      `}]],209232),e.s(["getTtsExamples",0,({slug:e,voice:a,responseFormat:o})=>{let s=a??"alloy",l=`output.${o??"mp3"}`,u=o?`,
    responseFormat: "${o}"`:"",c=o?`
    ResponseFormat: components.ResponseFormatEnum${function(e){switch(e){case"mp3":default:return"Mp3";case"pcm":return"Pcm"}}(o)}.ToPointer(),`:"",d=o?`,
  response_format="${o}"`:"",p=o?`,
    "response_format": "${o}"`:"",m=o?`
            response_format: '${o}',`:"",f=o?`,
            response_format: "${o}"`:"",g=o?`,
            "response_format": "${o}"`:"";return[{title:"openrouter-ts",language:"typescript",code:(0,n.normalizeIndentation)(`
import { OpenRouter } from "@openrouter/sdk";
import fs from "fs";

const openrouter = new OpenRouter({
  apiKey: "${t.API_KEY_REF}"
});

const stream = await openrouter.tts.createSpeech({
  speechRequest: {
    model: "${e}",
    input: "Hello! This is a text-to-speech test.",
    voice: "${s}"${u}
  }
});

const reader = stream.getReader();
const chunks: Uint8Array[] = [];
while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  chunks.push(value);
}
const totalLength = chunks.reduce((sum, c) => sum + c.length, 0);
const buffer = new Uint8Array(totalLength);
let offset = 0;
for (const chunk of chunks) {
  buffer.set(chunk, offset);
  offset += chunk.length;
}
await fs.promises.writeFile("${l}", buffer);
console.log("Audio saved to ${l}");
      `,{baseIndent:8})},{title:"openrouter-go",language:"go",code:(0,n.normalizeIndentation)(`
package main

import (
  "context"
  "io"
  "log"
  "os"

  openrouter "github.com/OpenRouterTeam/go-sdk"
  "github.com/OpenRouterTeam/go-sdk/models/components"
)

func main() {
  ctx := context.Background()

  s := openrouter.New(
    openrouter.WithSecurity(os.Getenv("OPENROUTER_API_KEY")),
  )

  res, err := s.Tts.CreateSpeech(ctx, components.SpeechRequest{
    Model: "${e}",
    Input: "Hello! This is a text-to-speech test.",
    Voice: "${s}",${c}
  })
  if err != nil {
    log.Fatal(err)
  }
  defer res.Close()

  out, err := os.Create("${l}")
  if err != nil {
    log.Fatal(err)
  }
  defer out.Close()

  if _, err := io.Copy(out, res); err != nil {
    log.Fatal(err)
  }
  log.Println("Audio saved to ${l}")
}
      `,{baseIndent:8})},{title:"openai-python",language:"python",code:(0,n.normalizeIndentation)(`
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="${t.API_KEY_REF}",
)

with client.audio.speech.with_streaming_response.create(
  extra_headers={
    ${(0,i.getHeaderLines)({commentPrefix:"#"}).join("\n    ")}
  },
  model="${e}",
  input="Hello! This is a text-to-speech test.",
  voice="${s}"${d}
) as response:
  response.stream_to_file("${l}")
      `,{baseIndent:8})},{title:"python",language:"python",code:(0,n.normalizeIndentation)(`
import requests

response = requests.post(
  url="https://openrouter.ai/api/v1/audio/speech",
  headers={
    "Authorization": "Bearer ${t.API_KEY_REF}",
    "Content-Type": "application/json",
    ${(0,i.getHeaderLines)({commentPrefix:"#"}).join("\n    ")}
  },
  json={
    "model": "${e}",
    "input": "Hello! This is a text-to-speech test.",
    "voice": "${s}"${p}
  }
)

with open("${l}", "wb") as f:
  f.write(response.content)
print(f"Audio saved. Generation ID: {response.headers.get('X-Generation-Id')}")
      `,{baseIndent:8})},{title:"openai-typescript",language:"typescript",code:`
        import OpenAI from 'openai';
        import fs from 'fs';

        const client = new OpenAI({
          baseURL: 'https://openrouter.ai/api/v1',
          apiKey: '${t.API_KEY_REF}',
          defaultHeaders: {
            ${(0,i.getHeaderLines)({}).join("\n            ")}
          },
        });

        async function main() {
          const response = await client.audio.speech.create({
            model: '${e}',
            input: 'Hello! This is a text-to-speech test.',
            voice: '${s}',${m}
          });

          const buffer = Buffer.from(await response.arrayBuffer());
          await fs.promises.writeFile('${l}', buffer);
          console.log('Audio saved to ${l}');
        }

        main();
      `},{title:"typescript",language:"typescript",code:`
        const response = await fetch("https://openrouter.ai/api/v1/audio/speech", {
          method: "POST",
          headers: {
            "Authorization": \`Bearer \${${t.API_KEY_REF}}\`,
            "Content-Type": "application/json",
            ${(0,i.getHeaderLines)({siteUrl:i.SITE_URL_REF,siteName:i.SITE_NAME_REF}).join("\n            ")}
          },
          body: JSON.stringify({
            model: "${e}",
            input: "Hello! This is a text-to-speech test.",
            voice: "${s}"${f}
          })
        });

        const audioBuffer = await response.arrayBuffer();
        const generationId = response.headers.get("X-Generation-Id");
        console.log(\`Generation ID: \${generationId}\`);
      `},{title:"curl",language:"shell",code:r.default`
        curl https://openrouter.ai/api/v1/audio/speech \\
          -H "Content-Type: application/json" \\
          -H "Authorization: Bearer $OPENROUTER_API_KEY" \\
          --output ${l} \\
          -d '{
            "model": "${e}",
            "input": "Hello! This is a text-to-speech test.",
            "voice": "${s}"${g}
          }'
      `}]}],186101)},274061,e=>{"use strict";var t=e.i(442427),n=e.i(860816),r=e.i(220988);let i="A serene mountain landscape at sunset with clouds drifting by",a=({slug:e,prompt:a=i,requestFields:o})=>{let s={model:e,...null===a?{}:{prompt:a},...o},l=e=>(0,n.indentObjectParam)(s,e+2).trimStart(),u=l(2).replaceAll(/^ {4}"(?<key>\w+)":/gm,"    $<key>:");return[{title:"python",language:"python",code:(0,n.normalizeIndentation)(`
import requests
import json
import time

# Step 1: Submit video generation request
response = requests.post(
  url="https://openrouter.ai/api/v1/videos",
  headers={
    "Authorization": "Bearer ${t.API_KEY_REF}",
    "Content-Type": "application/json",
  },
  data=json.dumps(${l(2)})
)

result = response.json()
job_id = result["id"]
polling_url = result["polling_url"]
print(f"Job submitted: {job_id}")

# Step 2: Poll for completion
while True:
  poll_response = requests.get(
    url=polling_url,
    headers={
      "Authorization": "Bearer ${t.API_KEY_REF}",
    }
  )
  status_data = poll_response.json()
  print(f"Status: {status_data['status']}")

  if status_data["status"] == "completed":
    for url in status_data.get("unsigned_urls", []):
      print(f"Video URL: {url}")
    break
  elif status_data["status"] == "failed":
    print(f"Error: {status_data.get('error', 'Unknown error')}")
    break

  time.sleep(5)
      `,{baseIndent:8})},{title:"typescript",language:"typescript",code:(0,n.normalizeIndentation)(`
// Step 1: Submit video generation request
const response = await fetch("https://openrouter.ai/api/v1/videos", {
  method: "POST",
  headers: {
    "Authorization": "Bearer ${t.API_KEY_REF}",
    "Content-Type": "application/json",
  },
  body: JSON.stringify(${u}),
});

const result = await response.json();
const jobId = result.id;
const pollingUrl = result.polling_url;
console.log("Job submitted:", jobId);

// Step 2: Poll for completion
const poll = async () => {
  while (true) {
    const pollResponse = await fetch(pollingUrl, {
      headers: {
        "Authorization": "Bearer ${t.API_KEY_REF}",
      },
    });
    const statusData = await pollResponse.json();
    console.log("Status:", statusData.status);

    if (statusData.status === "completed") {
      for (const url of statusData.unsigned_urls ?? []) {
        console.log("Video URL:", url);
      }
      return;
    }

    if (statusData.status === "failed") {
      console.error("Error:", statusData.error ?? "Unknown error");
      return;
    }

    await new Promise((resolve) => setTimeout(resolve, 5000));
  }
};

await poll();
      `,{baseIndent:8})},{title:"curl",language:"shell",code:r.default`
        # Step 1: Submit video generation request
        curl https://openrouter.ai/api/v1/videos \\
          -H "Content-Type: application/json" \\
          -H "Authorization: Bearer $OPENROUTER_API_KEY" \\
          -d '${l(10)}'

        # Response includes a polling_url. Use it to check status:
        # curl <polling_url> -H "Authorization: Bearer $OPENROUTER_API_KEY"
      `}]};e.s(["buildVideoGenerationExamples",0,a,"getVideoGenerationExamples",0,({slug:e,duration:t,size:n})=>a({slug:e,requestFields:{...t?{duration:t}:{},...n?{size:n}:{}}})])},191463,e=>{"use strict";e.s(["TTSResponseFormat",0,{Mp3:"mp3",Pcm:"pcm"}])},214703,e=>{"use strict";var t=e.i(764838);let n=t.forwardRef(function({title:e,titleId:n,...r},i){return t.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 24 24",fill:"currentColor","aria-hidden":"true","data-slot":"icon",ref:i,"aria-labelledby":n},r),e?t.createElement("title",{id:n},e):null,t.createElement("path",{fillRule:"evenodd",d:"M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25Zm-1.72 6.97a.75.75 0 1 0-1.06 1.06L10.94 12l-1.72 1.72a.75.75 0 1 0 1.06 1.06L12 13.06l1.72 1.72a.75.75 0 1 0 1.06-1.06L13.06 12l1.72-1.72a.75.75 0 1 0-1.06-1.06L12 10.94l-1.72-1.72Z",clipRule:"evenodd"}))});e.s(["XCircleIcon",0,n],214703)},430552,e=>{"use strict";var t=e.i(554331),n=e.i(361101),r=e.i(452473);function i(e){let i,a,o=(0,n.c)(4),{className:s}=e;return o[0]!==s?(i=(0,r.cn)("braille-sequence inline-flex w-4 shrink-0 justify-start font-mono text-sm leading-none text-muted-foreground",s),o[0]=s,o[1]=i):i=o[1],o[2]!==i?(a=(0,t.jsx)("span",{"aria-hidden":!0,className:i}),o[2]=i,o[3]=a):a=o[3],a}function a(e){let i,a,o,s,l,u,c=(0,n.c)(12);c[0]!==e?({className:i,label:a,shouldShimmer:s,...o}=e,c[0]=e,c[1]=i,c[2]=a,c[3]=o,c[4]=s):(i=c[1],a=c[2],o=c[3],s=c[4]);let d=void 0===s||s?"processing-label":"";return c[5]!==i||c[6]!==d?(l=(0,r.cn)(d,"relative inline-block overflow-hidden text-sm font-medium text-muted-foreground",i),c[5]=i,c[6]=d,c[7]=l):l=c[7],c[8]!==a||c[9]!==o||c[10]!==l?(u=(0,t.jsx)("span",{...o,className:l,"data-label":a,children:a}),c[8]=a,c[9]=o,c[10]=l,c[11]=u):u=c[11],u}function o(){let e,r=(0,n.c)(1);return r[0]===Symbol.for("react.memo_cache_sentinel")?(e=(0,t.jsx)("style",{children:"\n      .braille-sequence::before {\n        animation: brailleFrames 960ms steps(1, end) infinite;\n        content: '⠋';\n      }\n\n      .processing-label::after {\n        animation: processingTextShimmer 1600ms ease-in-out infinite;\n        background: linear-gradient(\n          90deg,\n          transparent 0%,\n          hsl(var(--foreground)) 42%,\n          hsl(var(--primary)) 50%,\n          hsl(var(--foreground)) 58%,\n          transparent 100%\n        );\n        background-clip: text;\n        background-repeat: no-repeat;\n        background-size: 45% 100%;\n        color: transparent;\n        content: attr(data-label);\n        inset: 0;\n        position: absolute;\n        -webkit-background-clip: text;\n        -webkit-text-fill-color: transparent;\n      }\n\n      @keyframes brailleFrames {\n        0% {\n          content: '⠋';\n        }\n        10% {\n          content: '⠙';\n        }\n        20% {\n          content: '⠹';\n        }\n        30% {\n          content: '⠸';\n        }\n        40% {\n          content: '⠼';\n        }\n        50% {\n          content: '⠴';\n        }\n        60% {\n          content: '⠦';\n        }\n        70% {\n          content: '⠧';\n        }\n        80% {\n          content: '⠇';\n        }\n        90%,\n        100% {\n          content: '⠏';\n        }\n      }\n\n      @keyframes processingTextShimmer {\n        from {\n          background-position: -80% 0;\n        }\n        to {\n          background-position: 180% 0;\n        }\n      }\n\n      @media (prefers-reduced-motion: reduce) {\n        .braille-sequence::before {\n          animation: none;\n          content: '⠿';\n        }\n\n        .processing-label::after {\n          animation: none;\n          content: '';\n        }\n      }\n    "}),r[0]=e):e=r[0],e}e.s(["ProcessingBrailleSequence",0,i,"ProcessingIndicator",0,function(e){let s,l,u,c,d,p,m=(0,n.c)(11),{className:f,label:g}=e,h=void 0===g?"Processing":g;return m[0]!==f?(s=(0,r.cn)("inline-flex items-center justify-start gap-2",f),m[0]=f,m[1]=s):s=m[1],m[2]===Symbol.for("react.memo_cache_sentinel")?(l=(0,t.jsx)(i,{}),m[2]=l):l=m[2],m[3]!==h?(u=(0,t.jsx)(a,{label:h}),m[3]=h,m[4]=u):u=m[4],m[5]!==s||m[6]!==u?(c=(0,t.jsxs)("div",{role:"status","aria-live":"polite",className:s,children:[l,u]}),m[5]=s,m[6]=u,m[7]=c):c=m[7],m[8]===Symbol.for("react.memo_cache_sentinel")?(d=(0,t.jsx)(o,{}),m[8]=d):d=m[8],m[9]!==c?(p=(0,t.jsxs)(t.Fragment,{children:[c,d]}),m[9]=c,m[10]=p):p=m[10],p},"ProcessingIndicatorStyles",0,o,"ProcessingShimmerLabel",0,a])},516738,e=>{e.v(t=>Promise.all(["static/chunks/14odpxd-x1_gq.js"].map(t=>e.l(t))).then(()=>t(471893)))},386693,e=>{e.v(t=>Promise.all(["static/chunks/3zxzg8b5kgdxf.js","static/chunks/1hlc7dhl6ez72.js"].map(t=>e.l(t))).then(()=>t(766210)))},392390,e=>{e.v(t=>Promise.all(["static/chunks/1sih2p1mwxd3j.js"].map(t=>e.l(t))).then(()=>t(157459)))},304241,e=>{e.v(t=>Promise.all(["static/chunks/1ooune10ne0u5.js"].map(t=>e.l(t))).then(()=>t(405996)))},266595,e=>{e.v(e=>Promise.resolve().then(()=>e(735961)))},542263,e=>{e.v(t=>Promise.all(["static/chunks/2a41qei4fumma.js","static/chunks/2h1jz0xmqaos1.js","static/chunks/39qp28b8fvmja.css"].map(t=>e.l(t))).then(()=>t(977864)))}]);

//# sourceMappingURL=2t32ru7rrsdbh.js.map
//# chunkId=019f9c7a-132c-7d20-b6d9-c3dcc3e8588e