var getADUser = function (user, opts) {

    return new Promise(resolve, reject){

    var sAMAccountName = user;
    var ad = new ActiveDirectory(config);

    ad.findUser(opts, sAMAccountName, function (err, user) {
        if (err) {
            console.log('ERROR: ' + JSON.stringify(err));
            reject(error)
            return;
        }
        if (!user) {
            console.log('User: ' + sAMAccountName + ' not found.');
        } else {
            if (user.userAccountControl == 514) {
                user.userAccountControl = 'Disabled'
            } else {
                user.userAccountControl = 'Active'
            }
            user.pwdLastSet = ${moment(fileTime(user.pwdLastSet))} - ${moment(fileTime(user.pwdLastSet)).fromNow()}
            if (user.lastLogonTimestamp) {
                user.lastLogonTimestamp = ${moment(fileTime(user.lastLogonTimestamp))} - ${moment(fileTime(user.lastLogonTimestamp)).fromNow()}
            }
            if (user.lastLogon) {
                user.lastLogon = ${moment(fileTime(user.lastLogon))} - ${moment(fileTime(user.lastLogon)).fromNow()}
            }
            console.log(user)

            resolve (user)
        }
    });

  }

}
