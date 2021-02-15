class A {
    bar: string; // Initialized to undefined
    prop?: string; // Initialized to undefined
    prop1!: string // Initialized to undefined
    constructor(){
        this.bar = "";
        this.prop = "";
        this.prop1 = "";
    }

    add(a:number, b:number):number {
        return a+b;
    }
}


const x: number = 0;

export {A};
