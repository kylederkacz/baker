function MediaCtrl($scope, api) {
    api.collection.query(function (result) {
        $scope.collections = result.objects;
    });

    $scope.collectionTypes = {
        'V': 'film',
        'A': 'music',
        'P': 'picture'
    };
}