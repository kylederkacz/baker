var app = angular.module('system', ['ngResource'])
    .config(['$interpolateProvider', function($interpolateProvider) {
        $interpolateProvider.startSymbol('[{');
        $interpolateProvider.endSymbol('}]');
    }])
    .factory('system', function ($resource) {
        var System = $resource(
            '/api/system/:command',
            { query: { method: 'GET', isArray: false }}
        );
        return System;
    });
// Directives



// Routing
app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/', { templateUrl: '/system', controller: SystemCtrl })

        // Configuration
        .when('/users', { templateUrl: '/system/users', controller: SystemCtrl })
        .when('/network', { templateUrl: '/system/network', controller: SystemCtrl })

        // External Devices
        .when('/drives', { templateUrl: '/system/drives', controller: SystemCtrl })

        .otherwise({ redirectTo: '/' });
}]);
