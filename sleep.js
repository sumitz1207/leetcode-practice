async function sleep(millis: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, millis));
}



 let x = Date.now()
 sleep(100).then(() => console.log(Date.now() - x))
