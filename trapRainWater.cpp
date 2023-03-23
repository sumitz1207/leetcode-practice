int trap(int* h, int n) {
    int lev = 0, fin = 0;
    while (n--) {
        int low = *h < h[n] ? *h++ : h[n];
        if (low > lev) lev = low;
        fin += lev - low;
    }
    return fin;
}
