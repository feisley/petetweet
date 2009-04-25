// ActionScript file
package com.petetweet.client.events
{
	import flash.events.Event;

	public class ViewProfileEvent extends Event
	{
		public function ViewProfileEvent(uid:String, bubbles:Boolean=true, cancelable:Boolean=false)
		{
			super("ViewProfileEvent", bubbles, cancelable);
			
			this.uid = uid;
		}
		
		public var uid:String;
		
		override public function clone():Event {
			return new ViewProfileEvent(uid);
		}
		
	}
}