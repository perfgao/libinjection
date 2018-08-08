#ifndef __LIBINJECTION_JS_DATA_H__
#define __LIBINJECTION_JS_DATA_H__

typedef struct {
    char* word;
    char  type;
} keywords_t;

static const keywords_t js_keywords[] = {
    {"abort", 'f'},
    {"blur",  'f'},
    {"change",  'f'},
    {"click",  'f'},
    {"dblclick",  'f'},
    {"error",  'f'},
    {"focus",  'f'},
    {"keydown",  'f'},
    {"keypress",  'f'},
    {"keyup",  'f'},
    {"load",  'f'},
    {"mousedown",  'f'},
    {"mousemove",  'f'},
    {"mouseout",  'f'},
    {"mouseover",  'f'},
    {"mouseup",  'f'},
    {"readystatechange", 'f'},
    {"reset",  'f'},
    {"resize",  'f'},
    {"select",  'f'},
    {"submit",  'f'},
    {"unload",  'f'},
};

#endif
