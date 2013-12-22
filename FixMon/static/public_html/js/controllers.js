/* 
 Created on : Dec 8, 2013, 4:55:01 PM
 Author     : ashish
 */

var fixMonApp = angular.module('fixmon', ['restangular', 'fixmonFilters']);


fixMonApp.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl('/api/v1');
});



fixMonApp.controller('fixMonCtrl', function($scope, Restangular) {
    $scope.editMode = true;
    Restangular.all('column').getList().then(function(columns) {
        $scope.columns = columns.objects;
    });
    
    Restangular.all('fixMsg').getList().then(function(fixMsgs) {
        $scope.fixMsgs = fixMsgs.objects;
    });
});

fixMonApp.controller('columnCtrl', function($scope, Restangular) {
    $scope.editMode = true;
    Restangular.all('column').getList().then(function(columns) {
        $scope.columns = columns.objects;
    });
    
    Restangular.all('fixMsg').getList().then(function(fixMsgs) {
        $scope.fixMsgs = fixMsgs.objects;
    });
});