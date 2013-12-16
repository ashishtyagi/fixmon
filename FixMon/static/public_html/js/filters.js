/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
angular.module('fixmonFilters', []).filter('valueExtractor', function() {
    return function(fixmsg, column) {
        if(column.sourceType === 'json')
            return fixmsg[column.path];        
        return $($.parseXML(fixmsg['xml'])).find(column.path).text();   
    };
});



