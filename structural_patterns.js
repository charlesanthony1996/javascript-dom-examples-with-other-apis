// structural pattern

// scenario -> document editing application

// adapter pattern

class ShapeInterface {
    draw() {

    }
}


// existing interface
class Text {
    constructor(content) {
        this.content = content
    }

    displayText() {
        console.log(`Text: ${this.content}`)
    }
}

// adapter for text to treat it as a shape
class TextShapeAdapter extends ShapeInterface {
    constructor(text) {
        super()
        this.text = text
    }

    draw() {
        this.text.displayText()
    }
}


// composite pattern

class CompositeShape extends ShapeInterface {
    constructor() {
        super()
        this.children = []
    }

    add(shape) {
        this.children.push(shape)
    }

    draw() {
        this.children.forEach((shape) => shape.draw())
    }
}

// proxy pattern -> shape proxy
class ShapeProxy extends ShapeInterface {
    constructor(shape) {
        super();
        this.shape = shape;
    }

    draw() {
        this.shape.draw();
    }
}


// flyweight pattern -> shape factory
class ShapeFactory {
    constructor() {
        this.shapes = []
    }

    getShape(type) {
        if(!this.shapes[type]) {
            this.shapes[type] = new Shape(type)
        }
        return this.shapes[type]
    }
}


// abstraction
class Shape {
    constructor(renderer) {
        this.renderer = renderer
    }

    draw() {
        this.renderer.render()
    }
}

// implementation
class VectorRenderer {
    render() {
        console.log("Rendering in vector format")
    }
}

class RasterRenderer {
    render() {
        console.log("Rendering in raster format")
    }
}


// integration exampple

// create some shapes
const circle = new Shape(new VectorRenderer())
const square = new Shape(new RasterRenderer())


// wrap a text object as a shape
const text = new TextShapeAdapter(new Text("Hello, world!"))

// composite shapes
const composite = new CompositeShape()
composite.add(circle)
composite.add(square)
composite.add(text)

// proxy to control access
const shapeProxy = new ShapeProxy(composite)

shapeProxy.draw()
