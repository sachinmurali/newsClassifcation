'use strict';

angular.module('newsclassifier', [])

.controller('MainController', ['$http', '$scope',function($http, $scope){
  var self = this;
  $scope.GetArticles = function() {
    $http.get('/retrievearticles/').success(function(data, status, headers, config){
      // self.current_articles = JSON.parse(data[0]);
      var elements = []
      for(var i = 0; i < data.length; i++) {
        elements.push(JSON.parse(data[i])[0]);
      }
      console.log(elements[0]['fields']['article_category']);
      self.current_articles = [1,2,3,4,5];
      self.test = "Hello";
      // $scope.current_articles = elements[0]['fields']['article_category'];
    });
  }

}]);
