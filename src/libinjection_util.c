#include "libinjection_util.h"

static int nstrcasecmp(const char *a, const char *b, size_t n)
{
    char cb;

    for (; n > 0; a++, b++, n--) {
        cb = *b;

        if (cb >= 'A' && cb <= 'Z') {
            cb += 0x20;
        }

        if (*a != cb) {
            return *a - cb;
        } else if (*a == '\0') {
            return -1;
        }
    }

    return (*a == 0) ? 0 : 1;
}


char bsearch_keywords(const char *src, size_t len,
        const keywords_t *words, size_t numb)
{
    size_t pos;
    size_t left = 0;
    size_t right = numb - 1;

    while (left < right) {
        pos = (left + right) >> 1;

        /* arg0 = lower case only, arg1 = mixed case */
        if (nstrcasecmp(words[pos].word, src, len) < 0) {
            left = pos + 1;
        } else {
            right = pos;
        }
    }

    if ((left == right) && nstrcasecmp(words[left].word, src, len) == 0) {
        return words[left].type;
    } else {
        return CHAR_NULL;
    }
}
