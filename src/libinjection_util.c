#include "libinjection_util.h"

static int nstrcasecmp(const char *word, const char *src, size_t len)
{
    for (; len > 0; len--, word++, src++) {
        if (*word != *src) {
            return *word - *src;
        }

        if (*word == '\0') {
            return -1;
        }
    }

    return (*word == 0)? 0 : 1;
}

static char* str_lower(const char *src, size_t len) {
    char ch;
    char *p;
    char *new;

    if (src == NULL) {
        return NULL;
    }

    new = (char *)malloc(len + 1);
    if (!new) {
        return NULL;
    }

    for (p = new; len > 0; len--, src++, p++) {
        ch = *src;
        if (ch >= 'A' && ch <= 'Z') {
            ch -= 0x20;
        }

        *p = ch;
    }

    *p = '\0';

    return new;
}

char bsearch_keywords(const char *src, size_t len,
        const keywords_t *words, size_t numb)
{
    int    res;
    size_t pos;
    size_t left = 0;
    size_t right = numb - 1;
    char *psrc = str_lower(src, len);
    if (!psrc) {
        return CHAR_NULL;
    }

    while (left <= right) {
        pos = (left + right) >> 1;

        res = nstrcasecmp(words[pos].word, psrc, len);
        if (res < 0){
            left = pos + 1;
        } else if (res > 0){
            right = pos - 1;
        } else {
            free(psrc);
            return words[pos].type;
        }
    }

    free(psrc);

    return CHAR_NULL;
}
