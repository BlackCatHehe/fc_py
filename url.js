function getplayurl(_in_data) {
  if (_in_data.indexOf("{") < 0) {
    var encode_version = "jsjiami.com.v5",
      unthu = "__0xb5aef",
      __0xb5aef = [
        "wohHHQdR",
        "dyXDlMOIw5M=",
        "dA9wwoRS",
        "U8K2w7FvETZ9csKtEFTCjQ==",
        "wo7ChVE=",
        "VRrDhMOnw6I=",
        "wr5LwoQkKBbDkcKwwqk=",
      ];
    (function (_0x22b97e, _0x2474ca) {
      var _0x5b074e = function (_0x5864d0) {
        while (--_0x5864d0) {
          _0x22b97e["push"](_0x22b97e["shift"]());
        }
      };
      _0x5b074e(++_0x2474ca);
    })(__0xb5aef, 0x1ae);
    var _0x2c0f = function (_0x19a33a, _0x9a1ebf) {
      _0x19a33a = _0x19a33a - 0x0;
      var _0x40a3ce = __0xb5aef[_0x19a33a];
      if (_0x2c0f["initialized"] === undefined) {
        (function () {
          var _0x4d044c =
            typeof window !== "undefined"
              ? window
              : typeof process === "object" &&
                typeof require === "function" &&
                typeof global === "object"
              ? global
              : this;
          var _0x1268d6 =
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
          _0x4d044c["atob"] ||
            (_0x4d044c["atob"] = function (_0x2993de) {
              var _0x467e1d = String(_0x2993de)["replace"](/=+$/, "");
              for (
                var _0x22a01d = 0x0,
                  _0x1ee2a1,
                  _0x2cf5ea,
                  _0x3a84f7 = 0x0,
                  _0x5c0e64 = "";
                (_0x2cf5ea = _0x467e1d["charAt"](_0x3a84f7++));
                ~_0x2cf5ea &&
                ((_0x1ee2a1 =
                  _0x22a01d % 0x4 ? _0x1ee2a1 * 0x40 + _0x2cf5ea : _0x2cf5ea),
                _0x22a01d++ % 0x4)
                  ? (_0x5c0e64 += String["fromCharCode"](
                      0xff & (_0x1ee2a1 >> ((-0x2 * _0x22a01d) & 0x6))
                    ))
                  : 0x0
              ) {
                _0x2cf5ea = _0x1268d6["indexOf"](_0x2cf5ea);
              }
              return _0x5c0e64;
            });
        })();
        var _0x3c81da = function (_0x457f21, _0x6cb980) {
          var _0x133a9b = [],
            _0x749ec5 = 0x0,
            _0x3ceeee,
            _0x1df5a4 = "",
            _0x35a2a6 = "";
          _0x457f21 = atob(_0x457f21);
          for (
            var _0x9a0e47 = 0x0, _0x4a71aa = _0x457f21["length"];
            _0x9a0e47 < _0x4a71aa;
            _0x9a0e47++
          ) {
            _0x35a2a6 +=
              "%" +
              ("00" + _0x457f21["charCodeAt"](_0x9a0e47)["toString"](0x10))[
                "slice"
              ](-0x2);
          }
          _0x457f21 = decodeURIComponent(_0x35a2a6);
          for (var _0x2ef02e = 0x0; _0x2ef02e < 0x100; _0x2ef02e++) {
            _0x133a9b[_0x2ef02e] = _0x2ef02e;
          }
          for (_0x2ef02e = 0x0; _0x2ef02e < 0x100; _0x2ef02e++) {
            _0x749ec5 =
              (_0x749ec5 +
                _0x133a9b[_0x2ef02e] +
                _0x6cb980["charCodeAt"](_0x2ef02e % _0x6cb980["length"])) %
              0x100;
            _0x3ceeee = _0x133a9b[_0x2ef02e];
            _0x133a9b[_0x2ef02e] = _0x133a9b[_0x749ec5];
            _0x133a9b[_0x749ec5] = _0x3ceeee;
          }
          _0x2ef02e = 0x0;
          _0x749ec5 = 0x0;
          for (
            var _0xa5d5ef = 0x0;
            _0xa5d5ef < _0x457f21["length"];
            _0xa5d5ef++
          ) {
            _0x2ef02e = (_0x2ef02e + 0x1) % 0x100;
            _0x749ec5 = (_0x749ec5 + _0x133a9b[_0x2ef02e]) % 0x100;
            _0x3ceeee = _0x133a9b[_0x2ef02e];
            _0x133a9b[_0x2ef02e] = _0x133a9b[_0x749ec5];
            _0x133a9b[_0x749ec5] = _0x3ceeee;
            _0x1df5a4 += String["fromCharCode"](
              _0x457f21["charCodeAt"](_0xa5d5ef) ^
                _0x133a9b[(_0x133a9b[_0x2ef02e] + _0x133a9b[_0x749ec5]) % 0x100]
            );
          }
          return _0x1df5a4;
        };
        _0x2c0f["rc4"] = _0x3c81da;
        _0x2c0f["data"] = {};
        _0x2c0f["initialized"] = !![];
      }
      var _0x4222af = _0x2c0f["data"][_0x19a33a];
      if (_0x4222af === undefined) {
        if (_0x2c0f["once"] === undefined) {
          _0x2c0f["once"] = !![];
        }
        _0x40a3ce = _0x2c0f["rc4"](_0x40a3ce, _0x9a1ebf);
        _0x2c0f["data"][_0x19a33a] = _0x40a3ce;
      } else {
        _0x40a3ce = _0x4222af;
      }
      return _0x40a3ce;
    };
    var panurl = _in_data;
    var hf_panurl = "";
    const keyMP = 0x100000;
    const panurl_len = panurl["length"];
    for (var i = 0x0; i < panurl_len; i += 0x2) {
      var mn = parseInt(panurl[i] + panurl[i + 0x1], 0x10);
      mn = (mn + keyMP - (panurl_len / 0x2 - 0x1 - i / 0x2)) % 0x100;
      hf_panurl = String[_0x2c0f("0x0", "1JYE")](mn) + hf_panurl;
    }
    _in_data = hf_panurl;
    encode_version = "jsjiami.com.v5";
  }
  return _in_data;
}

const purl =
  "abe6e2d9a597d6a9d5d4cf9da1cfcfcc9f9f9e969c9a9698c59295bfbdbebb8f878b88bab6b8b78274bebab1bfae7b6db9abb9b2a8a5a57264a3b3a5af9b9eaa9a9a6759979397625460a08e915c4e9596898a564895888d889696814d3f7a7d493b7975774436797b6f733e30703b2d68392a7773767568";
console.log(getplayurl(purl));
