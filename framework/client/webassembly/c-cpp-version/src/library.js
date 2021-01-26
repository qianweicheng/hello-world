mergeInto(LibraryManager.library, {
    my_js: function () {
        console.log("This function is an extern function to C lib");
    },
});