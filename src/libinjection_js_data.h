#ifndef __LIBINJECTION_JS_DATA_H__
#define __LIBINJECTION_JS_DATA_H__

#include <stddef.h>

typedef struct {
    const char* word;
    const char  type;
} keywords_t;


static const keywords_t js_keywords[] = {
    {"abort", 'f'},
    {"beforeunload", 'f'},
    {"blur", 'f'},
    {"cached", 'f'},
    {"change", 'f'},
    {"click", 'f'},
    {"close", 'f'},
    {"contextmenu", 'f'},
    {"copy", 'f'},
    {"cut", 'f'},
    {"dblclick", 'f'},
    {"drag", 'f'},
    {"dragend", 'f'},
    {"dragenter", 'f'},
    {"dragleave", 'f'},
    {"dragover", 'f'},
    {"dragstart", 'f'},
    {"drop", 'f'},
    {"error", 'f'},
    {"focus", 'f'},
    {"hashchange", 'f'},
    {"input", 'f'},
    {"invalid", 'f'},
    {"keydown", 'f'},
    {"keypress", 'f'},
    {"keyup", 'f'},
    {"load", 'f'},
    {"loadeddata", 'f'},
    {"loadedmetadata", 'f'},
    {"loadend", 'f'},
    {"loadstart", 'f'},
    {"mark", 'f'},
    {"message", 'f'},
    {"mousedown", 'f'},
    {"mouseenter", 'f'},
    {"mouseleave", 'f'},
    {"mousemove", 'f'},
    {"mouseout", 'f'},
    {"mouseover", 'f'},
    {"mouseup", 'f'},
    {"noupdate", 'f'},
    {"obsolete", 'f'},
    {"offline", 'f'},
    {"online", 'f'},
    {"open", 'f'},
    {"pagehide", 'f'},
    {"pageshow", 'f'},
    {"paste", 'f'},
    {"pause", 'f'},
    {"play", 'f'},
    {"playing", 'f'},
    {"pointerlockchange", 'f'},
    {"pointerlockerror", 'f'},
    {"popstate", 'f'},
    {"progress", 'f'},
    {"ratechange", 'f'},
    {"readystatechange", 'f'},
    {"repeatevent", 'f'},
    {"reset", 'f'},
    {"resize", 'f'},
    {"scroll", 'f'},
    {"seeked", 'f'},
    {"select", 'f'},
    {"show", 'f'},
    {"stalled", 'f'},
    {"storage", 'f'},
    {"submit", 'f'},
    {"success", 'f'},
    {"suspend", 'f'},
    {"svgabort", 'f'},
    {"svgerror", 'f'},
    {"svgload", 'f'},
    {"svgresize", 'f'},
    {"svgscroll", 'f'},
    {"timeout", 'f'},
    {"timeupdate", 'f'},
    {"touchenter", 'f'},
    {"touchleave", 'f'},
    {"touchmove", 'f'},
    {"touchstart", 'f'},
    {"unload", 'f'},
    {"updateready", 'f'},
    {"waiting", 'f'},
    {"wheel", 'f'},
};

static const size_t js_keywords_len = 86;

#endif
