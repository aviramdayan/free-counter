window.__callback = function (data) 
{ 
  var append=[%append%]; // values:0/1 type: list
  var place='[%place%]'; // type: id selector
  var width='[%width%]'; // type: text
  var height='[%height%]'; //type: text
  

  if(append) 
  {
    jQuery(place).append('<img src="//free-counter.appspot.com/images/online.png" width="'+width+'" height="'+height+'">Online Visitors: '+data.online);
  }
  else 
  {
    jQuery(place).prepend('<img src="//free-counter.appspot.com/images/online.png" width="'+width+'" height="'+height+'">Online Visitors: '+data.online);
  }
  
}

function UUID(){}UUID.generate=function(){var a=UUID._getRandomInt,b=UUID._hexAligner;return b(a(32),8)+"-"+b(a(16),4)+"-"+b(16384|a(12),4)+"-"+b(32768|a(14),4)+"-"+b(a(48),12)};UUID._getRandomInt=function(a){if(a<0)return NaN;if(a<=30)return 0|Math.random()*(1<<a);if(a<=53)return(0|Math.random()*(1<<30))+(0|Math.random()*(1<<a-30))*(1<<30);return NaN};UUID._getIntAligner=function(a){return function(b,c){var d=b.toString(a),e=c-d.length,f="0";for(;e>0;e>>>=1,f+=f){if(e&1){d=f+d}}return d}};UUID._hexAligner=UUID._getIntAligner(16);UUID.FIELD_NAMES=["timeLow","timeMid","timeHiAndVersion","clockSeqHiAndReserved","clockSeqLow","node"];UUID.FIELD_SIZES=[32,16,16,8,8,48];UUID.parse=function(a){var b,c=/^(?:urn:uuid:|\{)?([0-9a-f]{8})-([0-9a-f]{4})-([0-9a-f]{4})-([0-9a-f]{2})([0-9a-f]{2})-([0-9a-f]{12})(?:\})?$/i;if(b=c.exec(a)){return(new UUID)._init(parseInt(b[1],16),parseInt(b[2],16),parseInt(b[3],16),parseInt(b[4],16),parseInt(b[5],16),parseInt(b[6],16))}else{return null}};UUID.prototype._init=function(){var a=UUID.FIELD_NAMES,b=UUID.FIELD_SIZES;var c=UUID._binAligner,d=UUID._hexAligner;this.intFields=new Array(6);this.bitFields=new Array(6);this.hexFields=new Array(6);for(var e=0;e<6;e++){var f=parseInt(arguments[e]||0);this.intFields[e]=this.intFields[a[e]]=f;this.bitFields[e]=this.bitFields[a[e]]=c(f,b[e]);this.hexFields[e]=this.hexFields[a[e]]=d(f,b[e]/4)}this.version=this.intFields.timeHiAndVersion>>12&15;this.bitString=this.bitFields.join("");this.hexString=this.hexFields[0]+"-"+this.hexFields[1]+"-"+this.hexFields[2]+"-"+this.hexFields[3]+this.hexFields[4]+"-"+this.hexFields[5];this.urn="urn:uuid:"+this.hexString;return this};UUID._binAligner=UUID._getIntAligner(2);UUID.prototype.toString=function(){return this.hexString};UUID.prototype.equals=function(a){if(!(a instanceof UUID)){return false}for(var b=0;b<6;b++){if(this.intFields[b]!==a.intFields[b]){return false}}return true};UUID.genV1=function(){var a=(new Date).getTime(),b=UUID._state;if(a!=b.timestamp){if(a<b.timestamp){b.sequence++}b.timestamp=a;b.tick=UUID._getRandomInt(4)}else if(Math.random()<UUID._tsRatio&&b.tick<9984){b.tick+=1+UUID._getRandomInt(4)}else{b.sequence++}var c=UUID._getTimeFieldValues(b.timestamp);var d=c.low+b.tick;var e=c.hi&4095|4096;b.sequence&=16383;var f=b.sequence>>>8|128;var g=b.sequence&255;return(new UUID)._init(d,c.mid,e,f,g,b.node)};UUID.resetState=function(){UUID._state=new UUID._state.constructor};UUID._tsRatio=1/4;UUID._state=new function(){var b=UUID._getRandomInt;this.timestamp=0;this.sequence=b(14);this.node=(b(8)|1)*1099511627776+b(40);this.tick=b(4)};UUID._getTimeFieldValues=function(a){var b=a-Date.UTC(1582,9,15);var c=b/4294967296*1e4&268435455;return{low:(b&268435455)*1e4%4294967296,mid:c&65535,hi:c>>>16,timestamp:b}};UUID.makeBackwardCompatible=function(){var a=UUID.generate;UUID.generate=function(b){return b&&b.version==1?UUID.genV1().hexString:a.call(UUID)};UUID.makeBackwardCompatible=function(){}}
var uid = $SA.GC('__BnEcc')
if(!uid)
{
  uid=UUID.genV1().hexString;
  $SA.SC('__BnEcc', uid, 30); 
}
              
var sid=window.location.hostname;
jQuery.getJSON('http://free-counter.appspot.com/get/?uid='+uid+'&s='+sid+'&callback=?');
