'use strict';

angular.module('newsclassifier', [])

.controller('MainController', ['$http', function($http){
  var self = this;
  self.GetArticles = function(cat) {
    $http({
      url: '/retrievearticles/',
      params: {category: cat}
    }).success(function(data, status, headers, config){
      // self.current_articles = JSON.parse(data[0]);
      var elements = []
      for(var i = 0; i < data.length; i++) {
        elements.push(JSON.parse(data[i])[0]);
      }
      // self.current_articles = [1,2,3,4,5];
      self.current_articles = elements;
    });
  };

  self.DisplayArticle = function(article) {
    self.current_article = article;
    $('.cat-list-pane').removeClass('col-md-9').addClass('col-md-3');
    $('.article-pane').show();
  };
}])
.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
  });
