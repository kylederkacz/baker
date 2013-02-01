var app = angular.module('media', ['ngResource'])
    .config(['$interpolateProvider', function($interpolateProvider) {
        $interpolateProvider.startSymbol('[{');
        $interpolateProvider.endSymbol('}]');
    }])
    .config(function ($httpProvider) {
        $httpProvider.defaults.headers.post['X-CSRFToken'] = $.cookie('csrftoken');
    })
    .factory('api', function ($resource) {
        var Collection = $resource(
            '/api/v1/collection',
            {format: 'json'},
            { query: { method: 'GET', isArray: false }}
        );
        return {
            collection: Collection
        };
    });


// Directives
app
    // Form Directives: js/directives/form.js
    .directive('fileBrowserInput', ngFileBrowserInput);



// Routing
app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/settings', { templateUrl: '/media/settings', controller: MediaCtrl })
        .when('/collections', { templateUrl: '/media/collections', controller: MediaCtrl })
        .when('/collections/create', { templateUrl: '/media/collections/create', controller: MediaCtrl })
        .when('/collections/edit/:collectionId', { templateUrl: function (params) {
            return '/media/collections/edit/' + params['collectionId'];
        }, controller: MediaCtrl })

        // Project routes

        .otherwise({ redirectTo: '/settings' });
}]);
