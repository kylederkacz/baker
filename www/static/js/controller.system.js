function SystemCtrl($scope, system) {
    $scope.drives = system.get({command: 'driveinfo'}, function (result) {
        $.each(result, function (drive, values) {
            percent = parseInt(values['usage'], 10);
            if (percent >= 90) {
                result[drive]['usage_state'] = 'danger';
            }
            else if (percent >= 70) {
                result[drive]['usage_state'] = 'warning';
            }
            else {
                result[drive]['usage_state'] = 'success';
            }
            console.log(result[drive]['usage_state']);
        });
        return result;
    });

    $scope.network = system.get({command: 'networkinfo'});
}
