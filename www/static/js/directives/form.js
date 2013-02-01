function ngFileBrowserInput() {
    var fileBrowserInputDefinitionObject = {
        link: function (scope, iElement, iAttrs, controller) {
            var data = $(iElement).data();
            console.log(data);
            $(iElement).fileTree(data, function (file) {
                console.log(file);
            });
        }
    };
    return fileBrowserInputDefinitionObject;
}