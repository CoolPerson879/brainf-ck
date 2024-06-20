import * as robot from 'robotjs';

async function autotype(text: string, delay: number = 100): Promise<void> {
    for (let char of text) {
        robot.keyTap(char);
        await sleep(delay);
    }
}

function sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Example usage
async function main() {
    const textToType = "Hello, world! This is an autotype program using TypeScript.";

    // Adjust delay (in milliseconds) between each keystroke
    const typingDelay = 50;

    // Perform autotyping
    await autotype(textToType, typingDelay);

    // Optionally, simulate pressing Enter at the end
    robot.keyTap('enter');
}

main().catch(err => console.error(err));
