function removeElement(n, val) {
    let c = 0;
    for (let i = 0; i < n.length; i++) {
        if (n[i] !== val) {
            n[c++] = n[i];
        }
    }
    return c;
}
