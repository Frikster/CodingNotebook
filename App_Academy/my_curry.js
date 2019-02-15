Function.prototype.myCurry = function (numArgs) {
    let args = [];
    let fcn = this;
    curr = function (arg) {
        args.push(arg);
        if (args.length === numArgs) {
            return fcn(...args);
        } else {
            return curr;
        }
    }
    return curr;
};