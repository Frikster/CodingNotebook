Function.prototype.inherits = function (Parent) {
    function Surrogate() { }
    Surrogate.prototype = Parent.prototype;
    this.prototype = new Surrogate();
    this.prototype.constructor = this; // Otherwise it will have the same constructor as superclass
};